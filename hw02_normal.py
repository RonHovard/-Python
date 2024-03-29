
import random

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

numbers = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for i in range((len(numbers))):
    x = numbers[i]
    if x > 0:
        radical = x ** 0.5
        if float.is_integer(radical):
            new_list.insert(i, int(radical))
        else:
            pass
    else:
        pass
print(new_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input('Введите сегодняшнюю дату в формате dd.mm.yyyy: ')
date_list = date.split('.')
day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвертое',
       '05': 'пятое', '06': 'шестое', '07': 'седьмое', '08': 'восьмое',
       '09': 'девятое', '10': 'десятое', '11': 'одинадцатое',
       '12': 'двенадцатое', '13': 'тринадцатое','14': 'четырнадцатое',
       '15': 'пятьнадцатое', '16': 'шестьнадцатое', '17': 'семнадцатое',
       '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
       '21': 'двадцать первое', '22': 'двадцать второе',
       '23': 'двадцать третье', '24': 'двадцать четвертое',
       '25': 'двадцать пятое', '26': 'двадцать шестое',
       '27': 'двадцать седьмое', '28': 'двадцать восьмое',
       '29': 'двадцать девятое', '30':'дридцатое', '31': 'тридцать первое'}
month = {'01': 'январь', '02': 'февраль', '03': 'март', '04': 'апрель',
         '05': 'май', '06': 'июнь', '07': 'июль', '08': 'август',
         '09': 'сентябрь', '10': 'октябрь', '11': 'ноябрь', '12': 'декабрь'}
print(f'Сегодня {day[date_list[0]]} {month[date_list[1]]} {date_list[2]} года')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

n = int(input('Введите длину списка произвольных целых чисел: '))
arbitrary_integers = []
i = 0
while i < n:
    x = random.randint(-100, 100)
    arbitrary_integers.insert(i, x)
    i += 1
print(arbitrary_integers)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# a)
lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = list(set(lst))
print(lst2)

# б)
