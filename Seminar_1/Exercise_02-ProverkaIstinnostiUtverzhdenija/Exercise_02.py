# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = 1
Y = 2
Z = 3
if (not (X or Y or Z)) == (not X and not Y and not Z):
    print('True')
else:
    print('False')
