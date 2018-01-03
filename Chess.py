# Шахматная ладья ходит по горизонтали или вертикали.
# Даны две различные клетки шахматной доски, определите, может ли ладья попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для
# первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print("ROOK YES")
else:
    print("ROOK NO")

# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки
# сначала для первой клетки, потом для второй клетки.
# Программа должна вывести YES, если из первой клетки ходом короля можно попасть во вторую или NO в противном случае.

if 1 <= (x1-x2)**2 + (y1-y2)**2 <= 2:
    print("KING YES")
else:
    print("KING NO")