# Напишите функцию которая принимает строку текста. Сформулируйте список с уникальными кодами Unicode каждого символа отсортированный по убыванию

def func(data):
    return sorted(set([ord(el) for el in data]), reverse=True)



print(func('abrakadabra'))
