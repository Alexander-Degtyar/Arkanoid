import math
import pickle

import ball
import brick
import pad
import window


class Controller:
	"""Класс Контроллер.
	Сущность, управляющая игровыми объектами (мяч, ракетка, кирпичи).
	Отслеживает состояние игры (победа, поражение, гол, попадание по кирпичу)."""
	
	def __init__(self, window_config, ball_config, pad_config, bricks_config_list):
		"""Конструктор Контроллера.
		Принимает объекты, которыми будет управлять контроллер: окно, мяч, ракетку, список кирпичей.
		Устанавливает начальное состояние игры:
		количество попыток игрока, нулевое начальное значение счета (разрушенных кирпичей).
		Сохраняет ссылки на контролируемые объекты."""
		self.HP = 3  # Три попытки
		self.score = 0  # Начальный нулевой счёт
		self.window = window.Window(window_config[0], window_config[1], window_config[2], )
		self.ball = ball.Ball(self.window, ball_config[0], ball_config[1], ball_config[2], ball_config[5])
		self.ball.set_speed(ball_config[3], ball_config[4])
		self.pad = pad.Pad(self.window, pad_config[0], pad_config[1], pad_config[2])
		self.brick_list = [brick.Brick(self.window, brick_config[0], brick_config[1], brick_config[2], brick_config[3],
		                               brick_config[4]) for brick_config in bricks_config_list]
		self.max_score = len(self.brick_list)  # Счёт, при котором игрок победит
		# Привязка нажатия и отпускания клавиш к функции управления скоростью ракетки:
		self.window.canvas.bind("<KeyPress>", self.pad_speed_control)
		self.window.canvas.bind("<KeyRelease>", self.pad_speed_control)
	
	def main(self):
		"""Главная функция"""
		self.ball_movement()  # Двигать мяч
		self.pad_movement()  # Двигать ракетку
		self.window.after(50, self.main)  # Повторно вызвать главную функцию через 50 мсек
	
	def is_touch(self):
		"""Метод проверяет, касается ли мяч ракетки.
		Возвращает bool."""
		return (self.pad.get_coord('left') <= self.ball.get_coord('center-x') <= self.pad.get_coord('right')) and (
				self.pad.get_coord('top') <= self.ball.get_coord('bottom') <= self.pad.get_coord('bottom'))
	
	def get_touch_position(self):
		"""Метод возвращает координату X точки касания мяча с ракеткой."""
		return self.pad.get_coord("right") - self.ball.get_coord("center-x")
	
	def is_hit(self, brick):
		"""Метод проверяет, катается ли мяч кирпича.
		Возвращает сторону, которой произошло касание."""
		# Цикл проверки касания по всей окружности мяча с шагом в 90 градусов.
		for angle in range(0, 360, 90):
			# Вычисление координат X и Y точки на окружности под углом относительно начала отсчета.
			# Направление и начало отсчета аналогично тригонометричскому кругу - против часовой стрелки,
			# начиная с крайней правой точки окружности.
			dot_x = self.ball.get_coord('center-x') + self.ball.radius * math.cos(math.radians(angle))
			dot_y = self.ball.get_coord('center-y') + self.ball.radius * math.sin(math.radians(angle))
			# Проверяем касание мячом кирпича
			if ((brick.get_coord('left') <= dot_x <= brick.get_coord('right')) and (
					brick.get_coord('top') <= dot_y <= brick.get_coord('bottom'))):
				# Возвращаем сторону касания
				return {0: "right", 90: "top", 180: "left", 270: "bottom"}[angle]
	
	def is_goal(self):
		"""Проверка на гол.
		Возвращает bool, вылетел ли мяч ниже ракетки."""
		return self.ball.get_coord('bottom') > self.window.height
	
	def is_lose(self):
		"""Проверка на поражение.
		Возвращает bool, закончились ли игрока попытки."""
		return self.HP <= 0
	
	def is_win(self):
		"""Проверка на победу.
		Возвращает bool, достиг ли игрок счёта победы."""
		return self.score == self.max_score
	
	def ball_movement(self):
		"""Управление движением мяча."""
		# bounce off 3 walls
		# Отбитие мяча от стен
		if self.ball.get_coord('left') < 0 or self.ball.get_coord(
			'right') > self.window.width:  # Если мяч касается или входит в боковые стенки,
			self.ball.bounce('x')  # отбиться по горизонтали.
		elif self.ball.get_coord('top') < 0:  # Если мяч касается или входит в верхнюю стенку,
			self.ball.bounce('y')  # отбиться по вертикали
		# bounce off pad
		# Отбитие мяча от ракетки
		if self.is_touch():  # Если мяч касается или входит в ракетку,
			# отбиться под углом, который зависит от точки соприкосновения.
			self.ball.angular_bounce(30 + self.get_touch_position() * 0.6)
		# bounce off brick
		# Отбитие мяча от кирпичей
		for current_brick in self.brick_list:  # Для каждого кирпича
			
			hit_side = self.is_hit(current_brick)
			if hit_side:
				current_brick.destroy()  # Разрушить кирпич
				self.brick_list.remove(current_brick)  # Удалить кирпич из списка
				
				# Отбить мяч в зависимости от стороны касания:
				if hit_side in ("top", "bottom"):
					self.ball.bounce("y")
				else:
					self.ball.bounce("x")
				
				self.ball.boost()  # Ускорить мяч
				self.score += 1  # Увеличить счет
				# Вывести на экран текущий счет игрока:
				self.window.canvas.itemconfig(self.window.text_score, text = "Score:  " + str(self.score))
		
		if self.is_goal():  # Если мяч вылетел ниже ракетки
			self.HP -= 1  # Отнять одну попытку
			self.ball.set_position(self.window.get_center("x"),
			                       self.window.get_center("y"))  # Переместить мяч в центр окна
			self.pad.set_position(self.window.get_center("x"), self.window.height)  # Переместить ракетку в центр
			# Передать скорости по оси Y суммарную геометрическую скорость, которая была в момент гола:
			self.ball.set_speed(0, math.sqrt(self.ball.speed_x ** 2 + self.ball.speed_y ** 2))
			# Вывести на экран оставшееся количество попыток игрока:
			self.window.canvas.itemconfig(self.window.text_HP, text = "Health: " + str(self.HP))
		if self.is_lose():  # Если поражение
			self.ball.set_position(self.window.get_center("x"),
			                       self.window.get_center("y"))  # Переместить мяч в центр окна
			self.ball.set_speed(0, 0)  # Остановить мяч
			# Вывести на экран сообщение о поражении:
			self.window.canvas.itemconfig(self.window.text_end_game, text = "YOU LOSE", fill = "red")
		if self.is_win():  # Если победа
			self.ball.set_position(self.window.get_center("x"), self.window.get_center("y"))
			self.ball.set_speed(0, 0)
			# Вывести на экран сообщение о победе:
			self.window.canvas.itemconfig(self.window.text_end_game, text = "YOU WIN")
		# continue moving
		self.ball.fly()  # Продолжать полет мяча с текущей скоростью
	
	def pad_movement(self):
		"""Управление движением ракетки."""
		# Двигать ракетку с текущей скоростью
		self.pad.move()
	
	def pad_speed_control(self, event):
		if event.type == '2':  # Если нажата
			if event.keysym == "Left":  # клавиша Влево,
				self.pad.speed = -20  # установить отрицательную скорость
			elif event.keysym == "Right":  # клавиша Вправо,
				self.pad.speed = 20  # установить положительную скорость
		elif event.type == '3':  # Если отпустили
			if event.keysym in ("Left", "Right"):  # клавишу Влево или Вправо,
				self.pad.speed = 0  # аннулировать скорость


def load_level(file_name):
	file = open("./levels/" + file_name + ".dat", "rb")
	level = pickle.load(file)
	file.close()
	return level
