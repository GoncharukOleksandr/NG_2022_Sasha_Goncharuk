sec = float(input('Введіть кількість секунд: '))
seconds = sec % (24*3600*86400*2628002.88)
month = seconds // 2628002.88
seconds %= 2628002.88
days = seconds // 86400
seconds %=86400
hours = seconds // 3600
seconds %=3600
minuts = seconds//60
seconds %= 60
print('Місяців: ', month)
print('Дні: ', days)
print('Годин: ', hours)
print('Хвилин: ', minuts)
print('Секунд: ', seconds)