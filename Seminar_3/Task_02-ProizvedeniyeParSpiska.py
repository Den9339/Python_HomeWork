# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_original = [2, 3, 4, 5, 6]

if len(list_original) % 2 == 0:
    len_of_list = len(list_original) // 2
else:
    len_of_list = len(list_original) // 2 + 1

for index in range(len_of_list):
    mult_of_elements = list_original[index] * list_original[len(list_original) - 1 - index]
    print(mult_of_elements)