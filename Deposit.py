# Пользователь делает вклад в размере X гривен сроком на years лет под 10% годовых (каждый год
# размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в
# следующем году тоже будут проценты).
# Написать функцию bank, принимающая аргументы X и years, и возвращающую сумму, которая будет
# на счету пользователя.

def bank(x, year):
    i = 1
    while i < year:
        x += x*0.1
        i += 1
        res = x
    return res

grn = float(input("Enter sum of your deposit; "))
years = int(input("Enter count of years: "))

total = bank(grn, years)
print("%.2f" % total)