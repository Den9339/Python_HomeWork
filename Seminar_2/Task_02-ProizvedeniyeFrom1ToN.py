# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def list_from(number: int) -> list:
    list = []
    multiply = 1
    for i in range (1, number+1):
        multiply *= i
        list.append(multiply)
    return list

N = int(input('Введите число N: '))
print(list_from(N))