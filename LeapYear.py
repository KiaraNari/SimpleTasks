
# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True,
# если год високосный, и False иначе.

def is_year_leap(_year):
    print((_year%4)==0)

year = int(input("Enter year you want check: "))
is_year_leap(year)