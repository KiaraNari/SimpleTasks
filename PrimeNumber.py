# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(num):
    n = 2
    while num % n != 0:
        n += 1
    return num == n

your_num = (int(input("Enter the num from 0 to 1000: ")))
print(is_prime(your_num))
