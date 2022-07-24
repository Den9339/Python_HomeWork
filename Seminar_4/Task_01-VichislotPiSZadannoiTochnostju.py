# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$

import math


def chislo_after_dot(list: list) -> int:
    for i in range(len(list)):
        chislo_after_dot = len(list[1])
    return chislo_after_dot


d = str(input('Введите через "." число для выявления точности вывода числа pi: ')).split('.')
print(f'Точность в символах числа pi = {chislo_after_dot(d)} ')
print(round(math.pi, chislo_after_dot(d)))
