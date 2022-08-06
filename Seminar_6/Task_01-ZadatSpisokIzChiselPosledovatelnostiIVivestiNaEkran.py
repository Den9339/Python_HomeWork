# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите n: '))

posledovatelnost = lambda i: (1 + 1/i)**i
list_of_posledovatelnost = [round(posledovatelnost(i), 2) for i in range(1, n+1)]

def sum_of_posledovaelnost(list: list) -> float:
    sum = 0
    for i in list:
        sum+=i
    return round(sum, 2)

print(f'Список: {list_of_posledovatelnost}')
print(f'Сумма: {sum_of_posledovaelnost(list_of_posledovatelnost)}')