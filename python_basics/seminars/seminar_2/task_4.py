# Задача №4. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# Получаем числа, разбиваем на список строк(split), функция map применяет int к каждому элементу списка(вернет не список, а объект поддерживающий итерации) и делаем из него список(list)
data = [5, 1, 6, 5, 9]
# list(map(int, input('Введите числа через пробел: ').split()))
max_num = data[0]
min_num = data[0]

# Перебираем каждый элемент списка

for i in data:
    # Если текущий элемент больше max_num, то меняем max_num
    if i > max_num:
        max_num = i
    # Если текущий элемент меньше min_num, то меняем min_num
    if i < min_num:
        min_num = i

print(min_num, max_num)


# # Перебираем каждый элемент списка

# for i in range(1, len(data)):
#     # Если текущий элемент больше max_num, то меняем max_num
#     if data[i] > max_num:
#         max_num = data[i]
#     # Если текущий элемент меньше min_num, то меняем min_num
#     if data[i] < max_num and data[i] < min_num:
#         min_num = data[i]

# print(min_num, max_num)

def func(data=[5, 1, 6, 5, 9], max_num=data[0], min_num=data[0]):
    if len(data) == 0:
        return max_num, min_num
    if data[0] > max_num:
        max_num = data[0]
    if data[0] < min_num:
        min_num = data[0]
    return func(data[1:], max_num, min_num)


print(func(data))
