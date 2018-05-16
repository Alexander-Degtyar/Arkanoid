import pickle


brick_configs = [(100, 50, i, 100, "dark red") for i in range(100, 1500, 120)]

brick_configs.extend([(100, 50, i, 180, "dark green") for i in range(60, 1600, 120)])

file = open("./levels/level2.dat", "wb")
pickle.dump(brick_configs, file, False)
file.close()
