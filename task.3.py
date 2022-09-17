fibo = int(input('Введите предполагаемое число фибоначчи:  '))
n1 = 1
n2 = 1

for b in range (2,1000):
    i = 0
    while i < b - 2:
        summ = n1 + n2
        n1 = n2
        n2 = summ
        i += 1
        if fibo == n2:
            print('Да, число является числом фибоначчи')
            break
