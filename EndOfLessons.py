# В некоторой школе занятия начинаются в 9:00.
# Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут,
# а после 2-го, 4-го, 6-го и т.д. — 15 минут.
# Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
# Выведите два целых числа: время окончания урока в часах и минутах.

start = 9
minut = 0
num = int(input())
i = 0
while(i <= num):
    i += 1
    minut += 45
    if i == num:
        break
    if (i % 2 == 0):
        minut += 15
    else:
        minut += 5
print(9 + int(minut / 60))
print(minut % 60)