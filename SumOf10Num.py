# Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.

summa = 0

for i in range(10):
    a = int(input())
    summa += a
print(summa)