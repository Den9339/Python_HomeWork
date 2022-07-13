# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def posledovatelnost(n: float) -> list:
    list = []
    for i in range(1, n+1):
        list.append((1 + 1/i)**i)
    return list

def sum_of_posledovaelnost(n: list) -> float:
    sum = 0
    for i in list:
        sum+=i
    return round(sum, 2)

n = int(input('Введите n: '))
list = posledovatelnost(n)

print(f'Список: {posledovatelnost(n)}')
print(f'Сумма: {sum_of_posledovaelnost(list)}')