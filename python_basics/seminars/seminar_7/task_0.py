# Реализовать функцию, принимающую несколько параметров описывающих данные пользователя: имя, фамилия, год рождения, город проживания, емайл, телефон. Функция должна принимать параметры как именованные аргументы. Рализовать вывод данных о пользователе одной строкой

def func(**kwargs):
    return f'Сотрудник: {kwargs["name"]}, {kwargs["surname"]}'


print(func(name='Иван', surname='Иванов', age=18))
