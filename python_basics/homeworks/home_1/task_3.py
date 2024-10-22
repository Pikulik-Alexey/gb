# Задача 3. Счастливый билет
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,  которая проверяет счастливость билета с номером n и выводит на экран yes или no.

num = 385916
my_num = [int(i) for i in str(num)]
print(my_num)

if my_num[0] + my_num[1] + my_num[2] == my_num[3] + my_num[4] + my_num[5]:
    print('YES')
else:
    print('NO')


# Второе решение
# Ввод номера билета
n = int(input('Введите номер билета: '))
# Разделение числа на отдельные цифры
n1 = n // 100000  # первая цифра
n2 = (n % 100000) // 10000  # вторая цифра
n3 = (n % 10000) // 1000  # третья цифра
n4 = (n % 1000) // 100  # четвертая цифра
n5 = (n % 100) // 10  # пятая цифра
n6 = n % 10  # шестая цифра
# Проверка на счастливость билета
if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')  # Вывод 'yes', если билет счастливый
else:
    print('no')  # Вывод 'no', если билет не счастливый
