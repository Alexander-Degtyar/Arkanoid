class Brick:
	"""Класс Кирпич"""
	
	def __init__(self, window, width, height, pos_x, pos_y, color):
		"""Конструктор Кирпича принимает объект класса Window, в котором кирпич будет отрисовываться,
		ширину, высоту, координаты X и Y начальной позиции, цвет.
		Сохраняет значения размеров, ссылку на холст.
		Создает графический примитив (прямоугольник) для отрисовки кирпича на холсте."""
		self.__canvas = window.canvas
		self.__width = width
		self.__height = height
		self.__rectangle = self.__canvas.create_rectangle(pos_x - self.__width / 2, pos_y - self.__height / 2,
		                                                  pos_x + self.__width / 2, pos_y + self.__height / 2,
		                                                  fill = color, width = 2)
	
	@property
	def width(self):
		return self.__width
	
	@property
	def height(self):
		return self.__height
	
	def get_coord(self, side):
		"""Метод принимает строку-сторону. Возвращает координаты крайней точки запрашиваемой стороны."""
		if side in (0, 'l', 'left'):
			return self.__canvas.coords(self.__rectangle)[0]
		elif side in (1, 't', 'top'):
			return self.__canvas.coords(self.__rectangle)[1]
		elif side in (2, 'r', 'right'):
			return self.__canvas.coords(self.__rectangle)[2]
		elif side in (3, 'b', 'bottom'):
			return self.__canvas.coords(self.__rectangle)[3]
	
	def destroy(self):
		"""Метод разрушения кирпича. Удаляет кирпич на холсте."""
		self.__canvas.delete(self.__rectangle)
