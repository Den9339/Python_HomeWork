# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list_of_elements = [2, 3, 5, 9, 3, 5, 2, 2]
elements_nechet_pos = [list_of_elements[element] for element in range(1, len(list_of_elements), 2)] #if element%2 != 0]

sum = 0
for elements in elements_nechet_pos:
    sum += elements
    
print(f'На нечетной позиции находятся элементы {elements_nechet_pos}')
print(sum)