# Представлен список чисел. Необходимо вывести элементы исходного списка, значение которых больше предыдущего элемента.

data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 7, 70, 123, 55]

print([data[i] for i in range(1, len(data)) if data[i] > data[i - 1]])
