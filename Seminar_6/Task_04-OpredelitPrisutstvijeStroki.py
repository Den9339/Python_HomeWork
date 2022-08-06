# Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.


listt = ['232', 'sdfsd4', '23sdfsd4', 'sdfsdf650', '1', '4']
find_number = '23'
# find_array = [element for element in listt if find_number in element]
find_array = list(filter(lambda element: find_number in element, listt))

print(find_array)
