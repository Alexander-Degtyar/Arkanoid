import arkanoid


# Задание настроек окна:
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
WINDOW_COLOR = "dark grey"

# Задание настроек мяча:
BALL_RADIUS = 15
BALL_POSITION_X = WINDOW_WIDTH / 2
BALL_POSITION_Y = WINDOW_HEIGHT / 2
BALL_SPEED_X = 0
BALL_SPEED_Y = 10
BALL_COLOR = "dark green"

# Задание настроек ракетки:
PAD_WIDTH = 200
PAD_HEIGHT = 30
PAD_COLOR = "dark green"

# Создание кортежа настроек окна:
window_config = (WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_COLOR)

# Создание кортежа настроек мяча:
ball_config = (BALL_RADIUS, BALL_POSITION_X, BALL_POSITION_Y, BALL_SPEED_X, BALL_SPEED_Y, BALL_COLOR)

# Создание кортежа настроек ракетки:
pad_config = (PAD_WIDTH, PAD_HEIGHT, PAD_COLOR)

# Загрузка уровня (расположения кирпичей):
level = arkanoid.load_level("level2")

# Создание контроллера:
c = arkanoid.Controller(window_config, ball_config, pad_config, level)

# Вызов главной функции контроллера и цикла окна:
c.main()
c.window.mainloop()
