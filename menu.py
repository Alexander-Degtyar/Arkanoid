def choose_level():
	choise = int(input("""Выберите уровень:
	1 - 1-й уровень
	2 - 2-й уровень
	0 - Выйти"""))
	if choise not in (1, 2, 0):
		return None
	else:
		return choise
