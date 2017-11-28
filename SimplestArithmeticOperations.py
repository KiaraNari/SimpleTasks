
#Написать функцию arithmetic, принимающую 3 аргумента:
#первые 2 - числа, третий операция, которая должна быть произведена над ними.
#Если третий аргумент +, сложить их;
#если - -,то вычесть;
#* — умножить;
#/ — разделить(первое на второе).
#В остальных случаях вернуть строку “Неизвестная операция”.

def arithmetic(_num1, _num2, _act):
    if _act == '+':
        print("Result is ", (_num1 + _num2))
    elif _act == '-':
        print("Result is ", (_num1 - _num2))
    elif _act == '*':
        print("Result is ", (_num1*_num2))
    elif _act == '/':
        print("Result is ", (_num1 / _num2))
    else:
        print("Unknown operation")

num1 = int(input("Enter first num"))
num2 = int(input("Enter second num"))
act = input("Enter action")
arithmetic(num1, num2, act)