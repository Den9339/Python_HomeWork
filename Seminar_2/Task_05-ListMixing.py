# Реализуйте алгоритм перемешивания списка.

import random

def list_example(n: int) -> list:
    list = []
    for i in range(-n, n+1):
        list.append(i)
    return list

def list_mixing(list: list) -> list:
    for i in range(0, len(list)):
        mix_list_i = random.randint(0, len(list)-1)
        list[i], list[mix_list_i] = list[mix_list_i], list[i]

    return list
        

n = int(input('Введите количество элементов списка: '))
list = list_example(n)

print(list_example(n))
print(list_mixing(list))