# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Ввкдите координату X: '))
y = int(input('Ввкдите координату X: '))
if(x > 0 and y > 0):
    print('1 четверть')
if(x < 0 and y > 0):
    print('2 четверть')
if(x < 0 and y < 0):
    print('3 четверть')
if(x > 0 and y < 0):
    print('4 четверть')