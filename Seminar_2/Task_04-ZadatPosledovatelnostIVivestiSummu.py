# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции задаются с клавиатуры через пробел.
import random

def list_example(n: int) -> list:
    list = []
    for i in range(0, n):
        list.append(random.randint(-n, n))
    return list


def number_of_elements(positions: str) -> list:
    positions_list = positions.split(' ')
    for i in range(0, len(positions_list)):
        positions_list[i] = (int(positions_list[i]))
    return positions_list


def multiplicity_of_elements(list: list, positions_list: list) -> int:
    multiplicity = 1
    for i in positions_list:
        multiplicity *= list[i-1]
    return multiplicity


N = int(input('Введите N: '))
list = list_example(N)
print(f'Начальный список: \n {list}')
positions = input(f'Введите позиции элементов через пробел (от 1 до {N}):\n')
pos_list = number_of_elements(positions)
print(f'Произведение элементов на указанных позициях равно {multiplicity_of_elements(list, pos_list)}')