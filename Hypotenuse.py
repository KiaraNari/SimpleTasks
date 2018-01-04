# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.

from math import *

a, b = (int(input()) for i in range(2))
kv_gip = pow(a, 2) + pow(b, 2)

print(sqrt(kv_gip))