# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def veshestvennaya_chast(list: list) -> list:
    for index in range(len(list)):
        list[index] = round(list[index] - int(list[index]), 2)
    return list

def max_and_min_diff(list:list) -> float:
    max = list[0]
    min = list[0]
    diff = 0
    for index in range(1, len(list)):
        if(list[index] < min):
            min = list[index]
        if(list[index] > max):
            max = list[index]
    diff = round(max - min, 2)
    return diff

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)
veshestvennaya_chast(list)
print(max_and_min_diff(list))