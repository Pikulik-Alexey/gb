
def f_1(a, b):
    res = 1
    for _ in range(b):
        res *= a
    return res


def f_2(a, b, res=1):
    if b == 0:
        return res
    return f_2(a, b-1, res*a)


a, b = 3, 3

print(f_1(a, b))
print(f_2(a, b))
