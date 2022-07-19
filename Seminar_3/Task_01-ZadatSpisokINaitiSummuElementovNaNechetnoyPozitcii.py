# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_find(list: list) -> list:
    sum = 0
    for element in range(len(list)):
        if element%2 != 0:
            sum = sum + list[element]
            print(f'На нечетной позициии стоит элемент {list[element]}')
    print(f'Сумма элементов: {sum}')

list = [2, 3, 5, 9, 3]

sum_find(list)