
#Читаем 5 пар чисел и выводим их произведение
i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int (b)
    print(a * b)
    i += 1

# Если вводят 0 и 0 завершаем работу и ничего не выводим
i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int (b)
    if (a == 0) and (b == 0):
        break # оператор завершения, досрочно завершаем цикл
    print(a * b)
    i += 1
#можно так же break использовать в связке с else:    
else:
    print('Выведено 5 пар чисел')

#Continue - оператор перехода к
#следующей итерации циклп (при наличии)
i = 0
while i < 5:
    a, b = input().split()
    a = int(a)
    b = int (b)
    if (a == 0) and (b == 0):
        break # оператор завершения, досрочно завершаем цикл
    if (a == 0) or (b == 0):
        continue #переходим к следующей итерации, i не изменяется,
                 #на вход цикла подается то же значение i
    print(a * b)
    i += 1

#Практика: определить значение i после циклов
#1 Ответ 7
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
#2 Ответ 10  
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1

'''
Считываем целые числа с консоли по одному числу в строке.
Для каждого числа проверить:
1. число меньше 10, то пропускаем число;
2. число больше 100, то прекращаем считывать числа;
в остальных случаях вывод числа обратно на консоль в отдельной строке.
'''
a = 0
while a <= 100:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)
    
