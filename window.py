import tkinter


class Window:
	"""Класс Окно"""
	
	def __init__(self, width, height, color):
		"""Конструктор Окна принимает ширину окна, высоту окна, цвет фона.
		Создает холст. Создает заготовки различных надписей"""
		self.__width = width
		self.__height = height
		self.__root = tkinter.Tk()  # Создание окна
		self.__root.title("Alex Degtyar - Arkanoid")  # Изменение заголовка окна
		# Создание и сохранения холста, на котором будут располагаться все графические примитивы:
		self.__canvas = tkinter.Canvas(self.__root, width = width, height = height, bg = color)
		self.__canvas.pack()  # Упаковка холста в окно
		self.__canvas.focus_set()  # Фокусировка ввода (например, нажатия клавиш) на холсте.
		# Подготовка надписей для отображения текущего количества жизней,
		# счета разрушенных кирпичей и конца игры (победы или поражения).
		self.text_HP = self.__canvas.create_text(60, 20, fill = "dark red", text = "Health: 3", font = "Tahoma 18")
		self.text_score = self.__canvas.create_text(60, 50, fill = "dark red", text = "Score:  0", font = "Tahoma 18")
		self.text_end_game = self.__canvas.create_text(self.get_center("x"), self.get_center("y") + 100, fill = "green",
		                                               text = "", font = "Tahoma 62")
	
	@property
	def canvas(self):
		return self.__canvas
	
	@property
	def height(self):
		return self.__height
	
	@property
	def width(self):
		return self.__width
	
	def after(self, delay, func):
		self.__root.after(delay, func)
	
	def mainloop(self):
		self.__root.mainloop()
	
	def get_center(self, axis):
		"""Метод принимает строку - ось.
		Возвращает координату центра соответствующей оси."""
		if axis == "x":
			return self.width / 2
		elif axis == "y":
			return self.height / 2
