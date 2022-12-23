import math
a = float(input('Введіть перший коефіцієнт: '))
b = float(input('Введіть другий коефіцієнт: '))
c = float(input('Введіть вільний член: '))
print('Рівняння має вигляд: ', a, '*x^2 + ', b, 'x + ', c, ' = 0')
D = b*b - 4*a*c
if D>0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print('Перший корінь: ', x1)
    print('Другий корінь: ', x2)
elif D==0:
    x = -b/(2*a)
    print ('Корінь рівняння: ', x)
else:
    print ('Рівняння не має коренів.')