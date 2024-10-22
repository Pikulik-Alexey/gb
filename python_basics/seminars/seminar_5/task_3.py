# Задача №3. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# 2 3 5 7 11 13

def func_1(n):
    for el in range(2, n):
        if n % el == 0:
            return 'NO'
    return 'YES'


print(func_1(5))  # Output: yes


def func_2(n, el=2):
    if el < n:
        if n % el == 0:
            return 'NO'
        return func_2(n, el + 1)
    return 'YES'


print(func_2(5))  # Output: yes
