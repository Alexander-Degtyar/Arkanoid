import math


class Ball:
	"""Класс Мяч"""
	
	def __init__(self, window, radius, pos_x, pos_y, color):
		"""Конструктор Мяча принимает объект класса Window, в котором мяч будет отрисовываться,
		радиус мяча, начальную позицию по X и Y, цвет мяча.
		Задает мячу начальную скорость, сохраняет значения радиуса, ссылку на холст.
		Создает графический примитив (овал) для отрисовки мяча на холсте."""
		self.__speed_x = 0  # Скрорость по оси X
		self.__speed_y = 0  # Скорость по оси Y
		self.__radius = radius  # Радиус мяча
		self.__canvas = window.canvas  # Ссылка на холст
		self.__oval = self.__canvas.create_oval(pos_x - radius, pos_y - radius, pos_x + radius, pos_y + radius,
		                                        fill = color)
	
	@property
	def speed_x(self):
		return self.__speed_x
	
	@property
	def speed_y(self):
		return self.__speed_y
	
	@property
	def radius(self):
		return self.__radius
	
	def change_position(self, x, y):
		"""Метод принимает вектора по X и Y, на которые изменит текущее местоположение мяч."""
		self.__canvas.move(self.__oval, x, y)
	
	def set_position(self, x, y):
		"""Метод устанавливает мячу переданное местоположение по X и Y."""
		self.__canvas.coords(self.__oval, x - self.radius, y - self.radius, x + self.radius, y + self.radius)
	
	def fly(self):
		"""Метод перемещает мяч в зависимости от текущей скорости."""
		self.change_position(self.speed_x, self.speed_y)
	
	def get_coord(self, side):
		"""Метод принимает строку-сторону. Возвращает координаты крайней точки запрашиваемой стороны."""
		if side in (0, 'l', 'left'):  # Координата X левой стороны мяча.
			return self.__canvas.coords(self.__oval)[0]
		elif side in (1, 't', 'top'):  # Координата Y верхней стороны мяча.
			return self.__canvas.coords(self.__oval)[1]
		elif side in (2, 'r', 'right'):  # Координата X правой стороны мяча.
			return self.__canvas.coords(self.__oval)[2]
		elif side in (3, 'b', 'bottom'):  # Координата Y нижней стороны мяча.
			return self.__canvas.coords(self.__oval)[3]
		elif side in ('cx', 'center-x'):  # Координата X центра мяча.
			return self.get_coord('left') + self.radius
		elif side in ('cy', 'center-y'):  # Координата Y центра мяча.
			return self.get_coord('top') + self.radius
	
	def set_speed(self, x, y):
		"""Метод принимает числа - скорости по оси X и Y.
		Устанавливает мячу принятые скорости."""
		self.__speed_x = x
		self.__speed_y = y
	
	def boost(self):
		"""Метод увеличивает скорости мяча по двум осям на 10%."""
		self.__speed_x *= 1.1
		self.__speed_y *= 1.1
	
	def bounce(self, axis):
		"""Метод принимает строку - ось, по которой мяч отобьется.
		Изменяет скорость на противопожную по принятой оси."""
		if axis in (0, 'x'):
			self.__speed_x *= -1
		elif axis in (1, 'y'):
			self.__speed_y *= -1
	
	def angular_bounce(self, angle):
		summary_speed = math.sqrt(self.__speed_x ** 2 + self.__speed_y ** 2)
		self.__speed_x = summary_speed * math.cos(math.radians(angle))
		self.__speed_y = summary_speed * -math.sin(math.radians(angle))
