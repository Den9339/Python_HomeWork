# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

x1 = int(input('Введите координату x1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату x2: '))
y2 = int(input('Введите координату y2: '))

d = round((((x2-x1)**2) + ((y2-y1)**2))**0.5, 2)

print(d)