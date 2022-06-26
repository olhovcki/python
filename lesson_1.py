# Задание 7

a = 5
b = 56
day_counter = 0

while a < b:
    a = a * 0.1 + a
    day_counter += 1
    print(day_counter,'- й день:','%.2f'%a)



