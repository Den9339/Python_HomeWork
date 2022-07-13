# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def sum_find(chislo: float):
    sum = 0
    while chislo != 0:
        sum = chislo % 10 + sum
        chislo = chislo // 10
    return sum

chislo = float(input('Введите число: '))
print(f'Сумма цифр числа = {sum_find(chislo)}')