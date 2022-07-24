# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def unique_numbers_list(list: list) -> list:
    unique_list = []
    for number in list:
        count = 0
        for exam_number in list:
            if number == exam_number:
                count += 1
        if count == 1: 
            unique_list.append(number)
    return unique_list

list = [1, 2, 2, 3, 4, 3, 3, 6, 7, 8, 9, 8]
print(unique_numbers_list(list))