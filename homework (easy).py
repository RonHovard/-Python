# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

welcome = 'Добро пожаловать!'
print(welcome)
name = input('Введи своё имя: ')
print('Привет,', name, '!')

# Задача-2: Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

number = int(input('Введи число цифрами: '))
print(number + 2)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введи свой возраст: '))
if age >= 18:
    print('Доступ разрешён!')
else:
    print('Извини,', name, 'использование данного ресурса с 18 лет')