# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# специльные конструкторы, чтобы данные получить/записать
from csv import DictReader, DictWriter
from os.path import exists  # проверка на существование

# Функция получения информации о пользователе


class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    # Валидация
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя')
            second_name = input('Фамилия: ')
            if len(first_name) < 4:
                raise NameError('Слишком короткая фамилия')
            phone_number = input('Телефон: ')
            if len(phone_number) < 11:
                raise NameError('Слишком короткий номер телефона')
        except NameError as e:
            print(e)
        else:
            flag = True
            # возвращаем список
    return [first_name, second_name, phone_number]

# Функция создания файла


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:  # менеджер контекста
        f_w = DictWriter(data, fieldnames=[
                         'first_name', 'second_name', 'phone_number'])  # создание объекта с шапкой
        f_w.writeheader()

# Функция записи файлов


def write_file(file_name):
    user_data = get_info()
    res = read_file(file_name)
    new_obj = {
        'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    # делаем полную перезапись
    standart_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)  # список со словарями


def remove_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print('Введен неверный номер строки!!!')


def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=[
                         'first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)


file_name = 'phone.csv'

# Диспетчер


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            # проверка на наличие файла
            if not exists(file_name):  # если файла нет, то его создаем
                create_file(file_name)  # если файла нет, то его создаем
            write_file(file_name)  # если есть, то дозаписываем
        elif command == 'r':
            if not exists(file_name):
                print('Файл не найден, создайте его')
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print('Файл не найден, создайте его')
                continue
            remove_row(file_name)


main()
