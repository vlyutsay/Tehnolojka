import math
print ('Список операций: +, -, *, /, **, log(первое число = число, второе = основание), ceil(окр. в большую сторону), '
       'floor(окр. в меньшую сторону)')
func = input('Введите операцию из списка:  ')
x = float(input('Введите первое число:  '))
y = float(input('Введите второе число:  '))
if func == '+':
    print (x + y)
elif func == '-':
    print (x - y)
elif func == '*':
    print (x * y)
elif func == '/':
    print (x / y)
elif func == '**':
    print (x ** y)
elif func == 'log':
    print (math.log(x,y))
elif func == 'ceil':
    print (math.ceil(x))
    print (math.ceil(y))
elif func == 'floor':
    print (math.floor(x))
    print (math.floor(y))
else:
    print ('Ошибка, неправильная функция')