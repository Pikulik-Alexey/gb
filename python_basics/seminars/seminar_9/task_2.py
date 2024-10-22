# Задача №2. Решение в группах
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000

from pandas import read_csv

data = read_csv('california_housing_test.csv')
# 1. Проверить есть ли в файле пустые значения
print(data.isnull())
# Пустых нет
print(data.isnull().sum())
# 2. Показать median_house_value где median_income < 2
print(data[data['housing_median_age'] < 2]['median_house_value'])
# 3. Показать данные в первых 2 столбцах
# Если знаем заранее поля
print(data[['longitude', 'latitude']])
# Если не знаем
print(data.iloc[:, :2])
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000
print(data[(data['housing_median_age'] < 20)
      & (data['median_house_value'] > 70000)])
