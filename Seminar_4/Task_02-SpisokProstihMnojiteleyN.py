# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def find_simple_list(n: int) -> list:
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    return list


N = int(input('Введите натуральное число: '))
print(find_simple_list(N))
