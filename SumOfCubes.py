# По данному натуральному n вычислите сумму 13+23+33+...+n3.

n = int(input())
summa = 0

for i in range(n+1):
    summa += pow(i, 3)

print(summa)