# Задача №3. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)
# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

n = int(input('Введите число: '))
max_number = n
while n != 0:
    if n > max_number:
        max_number = n
    n = int(input('Введите число: '))

print(max_number)


# def func(n, max_number):
#     if n == 0:
#         return max_number
#     n = int(input('Введите число: '))
#     if n > max_number:
#         max_number = n
#     return func(n, max_number)


# n = int(input('Введите число: '))
# print(func(n, n))
