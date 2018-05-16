class Pad:
	"""Класс Ракетка"""
	
	def __init__(self, window, width, height, color):
		"""Конструктор Ракетки принимает объект класса Window, в котором ракетка будет отрисовываться,
		высоту, ширину и цвет ракетки.
		Задает ракетке начальную нулевую скорость, сохраняет значения размера, ссылку на холст.
		Создает графический примитив (прямоугольник) для отрисовки ракетки на холсте."""
		self.__speed = 0
		self.__width = width
		self.__height = height
		self.__canvas = window.canvas
		self.__rectangle = self.__canvas.create_rectangle(window.get_center("x") - self.__width / 2,
		                                                  window.height - 100 - self.__height / 2,
		                                                  window.get_center("x") + self.__width / 2,
		                                                  window.height - 100 + self.__height / 2, fill = color)
	
	@property
	def speed(self):
		return self.__speed
	
	@speed.setter
	def speed(self, new_speed):
		self.__speed = new_speed
	
	@property
	def width(self):
		return self.__width
	
	@property
	def height(self):
		return self.__height
	
	def change_position(self, x, y):
		"""Метод принимает вектора по X и Y, на которые изменит текущее местоположение ракетка."""
		self.__canvas.move(self.__rectangle, x, y)
	
	def set_position(self, x, y):
		"""Метод устанавливает ракетке переданное местоположение по X и Y."""
		self.__canvas.coords(self.__rectangle, x - self.width / 2, y - 100 - self.height / 2, x + self.width / 2,
		                     y - 100 + self.height / 2)
	
	def get_coord(self, side):
		"""Метод принимает строку-сторону. Возвращает координаты крайней точки запрашиваемой стороны."""
		if side in (0, 'l', 'left'):  # Координата X левой стороны мяча.
			return self.__canvas.coords(self.__rectangle)[0]
		elif side in (1, 't', 'top'):  # Координата Y верхней стороны мяча.
			return self.__canvas.coords(self.__rectangle)[1]
		elif side in (2, 'r', 'right'):  # Координата X правой стороны мяча.
			return self.__canvas.coords(self.__rectangle)[2]
		elif side in (3, 'b', 'bottom'):  # Координата Y нижней стороны мяча.
			return self.__canvas.coords(self.__rectangle)[3]
	
	def move(self):
		"""Метод перемещает ракетку в зависимости от текущей скорости."""
		self.change_position(self.speed, 0)
