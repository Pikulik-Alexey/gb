array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 80, 90, 52]
# Берем последний элемент
last = array.pop()
first = array.pop(0)

array.insert(0, last)
array.append(first)
print(array)
