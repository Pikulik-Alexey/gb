
def f_1(a, b):
    while b != 0:
        a += 1
        b -= 1
    return a


print(f_1(4, 5))


def f_2(a, b):
    if b == 0:
        return a
    return f_2(a+1, b-1)


print(f_2(4, 5))
