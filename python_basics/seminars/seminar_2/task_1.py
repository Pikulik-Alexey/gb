# Задача №1. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120
# 5! = 1 * 2 * 3 * 4 * 5

num = 5
f = 1
# while num > 1:
#     f *= num
#     num -= 1

# print(f)

# for el in range(1, num + 1):
#     f *= el

# print(f)


def fact(num, f=1):
    if num == 0:
        return f
    return fact(num-1, f*num)


print(fact(num))
