color = 'red'

if color == 'red':
    print('красный')
elif color == 'red':
    print('красный')
if color == 'red':
    print('красный')

# ----------------------------------------------------------------
a = 2
while a > 0:
    print(a)
    if a == 3:
        break
    a -= 1
else:
    print('Завершение цикла не по брейк')

# ----------------------------------------------------------------
my_str = 'jrhgiowehgjbpfxjko'
for el in my_str:
    print(el, end='')

print()
i = 0
while i < len(my_str):
    print(my_str[i], end='')
    i += 1
