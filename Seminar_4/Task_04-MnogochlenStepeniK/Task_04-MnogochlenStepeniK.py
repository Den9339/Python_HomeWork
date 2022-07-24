# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def string_of_polynomial(k: int) -> str:
    string = ''
    while k > 1:
        string += f'{random.randint(0, 100)}*x^{k} + '
        k -= 1
    string += f'{random.randint(0, 100)}*x + {random.randint(0, 100)} = 0'
    return(string)


k = int(input('Введите степень многочлена: '))


# path = 'Task_04-MnogochlenStepeniK\polynomial.txt'
# with open (path, 'w') as data:
#         data.write(string_of_polynomial(k))