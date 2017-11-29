from math import pow, sqrt
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью
# кортежа) : периметр квадрата, площадь квадрата и диагональ квадрата.

def square(_side):
    per = 4*_side
    sq = pow(_side, 2)
    diag = sqrt(2*sq)
    all_size = (per, sq, diag)
    return all_size

all_size = square(int(input("Enter side of square: ")))
print(all_size)