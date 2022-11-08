# Вычислить число c заданной точностью d

import random
num = random.uniform(0.5, 10.5)
degree = random.randint(-10, -1)
d = 10 ** degree

print(f'Число {num} с заданной точностью {d} равно {round(num, -degree)}')