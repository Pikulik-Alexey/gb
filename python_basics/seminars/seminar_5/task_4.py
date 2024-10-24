# Задача №4. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

data = '3 4'


def func_1(data):
    new_str = ''
    for elem in reversed(data):
        new_str += elem
    return new_str


print(func_1(data))


def func_2(data, new_str=''):
    if len(data) == 0:
        return new_str
    return func_2(data[:-1], new_str+data[-1])


print(func_2(data))
