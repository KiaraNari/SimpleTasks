# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит(зима, весна, лето или осень).

year = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}

def season(numOfMounth):
    return year[numOfMounth]
try:
    numberMounth = int(input("Enter number of mounth you need (1-12): "))
    result = season(numberMounth)
    print(result)
except Exception:
    print("Wrong data")
    numberMounth = int(input("Enter number of mounth you need (1-12): "))
    result = season(numberMounth)
    print(result)