# Задание 2

add_mi_sec = int(input('Введите время в секундах - '))
mi_sec = add_mi_sec % 60
mi_minute = add_mi_sec % 3600 // 60
mi_hour = add_mi_sec // 3600
print('%02d'% mi_hour, ':', '%02d'% mi_minute, ':', '%02d'% mi_sec)