# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def des_number_to_dvoichn(number: int) -> int:
    bit = number%2
    dvoichn = bit
    number = number//2
    i = 1
    while (number > 0):
        bit = number%2
        number = number//2
        dvoichn += bit*(10)**i
        i += 1
    return dvoichn

number = int(input('Введите десятичное число: '))
print(des_number_to_dvoichn(number))