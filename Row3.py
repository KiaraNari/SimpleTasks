# Даны два целых числа A и В, A>BA>B. Выведите все нечётные числа от A до B включительно, в порядке убывания.
# В этой задаче можно обойтись без инструкции if.

A = int(input())
B = int(input())

for i in range(A, B-1, -1):
    if i % 2 != 0:
        print(i)