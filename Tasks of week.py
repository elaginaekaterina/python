#Поиск минимума в списке
a = [int(i) for i in input().split()]
m = a[0]
for x in a:
    if m > x:
        m = x
print(m)

#Сапер
#Даны размеры поля для игры в сапер и
#координаты мин, стоящих на этом поле.
#Вывести поле игры на экран.
n, m , k = (int(i) for i in input().split())# Чтение размеров поля и числа мин
a = [[0 for j in range(m)] for i in range(n)] # заполнение 0
for i in range (k): #прочитываем k - пар чисел(координаты расположения мин)
    row, col = (int(i) - 1 for i in input().split()) # считываем данные массива
    a[row][col] = -1 #записываем -1 в нужную ячейку, расставляем мины
for i in range(n):  
    for j in range(m):
        if a[i][j] == 0: # в этой мины нет, поэтому считаем их вокруг
            for di in range(-1, 2): # смещение по i
                for dj in range (-1, 2): #смешение по j
                    ai = i + di
                    aj = +j +dj
                    #( ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1: #нашли мину
                        a[i][j] += 1
# Вывод результата
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()

'''
Напишите программу, которая считывает с консоли числа (по одному в строке)
до тех пор, пока сумма введённых чисел не будет равна 0 и
сразу после этого выводит сумму квадратов всех считанных чисел.
Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
после этого считывание продолжать не нужно.'''

a = int(input())
s = a
Skv = 0 + (a**2)
while s != 0:
    a = int(input())
    s = s + a
    Skv = Skv + (a**2)
    if s == 0:
        break
print(Skv)

'''
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число
n — столько элементов последовательности должна отобразить программа. На выходе ожидается
последовательность чисел, записанных через пробел в одну строку '''   
 
n = int(input())
m = []
for i in range(n):
    j = 0
    while j < i+1:
        m.append(i+1)
        j += 1
    if len(m) > n: break
m = m[0:n]
for i in m:
    print(i, end=' ')

'''
Напишите программу, которая считывает список чисел lst из первой строки
и число x из второй строки, которая выводит все позиции, на которых
встречается число x в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке,
вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.'''

lst = [int(i) for i in input().split()]
x = int(input())
for i in range(len(lst)):
               if lst[i] == x:
                   print(i, end=' ')
if x not in lst:
    print('Отсутствует')

'''
На вход подаётся прямоугольная матрица в виде
последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент
в позиции i, j равен сумме элементов первой матрицы на позициях (i-1,j), (i+1, j), (i,j-1), (i,j+1).
У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.'''

first = ''
second = []
while True:
    first = str(input())
    if first == 'end':
        break
    second.append([int(s) for s in first.split()])
li, lj = len(second), len(second[0])
new = [[sum([second[i-1][j],second[(i+1)%li][j],second[i][j-1],second[i][(j+1)%lj]]) for j in range(lj)] for i in range (li)]
for i in range(li):
    for j in range(lj):
        print(new[i][j], end=' ')
    print()

#Выведите таблицу размером n×n, заполненную числами от 1 до n^2
#по спирали, выходящей из левого верхнего угла и закрученной по
#часовой стрелке, как показано в примере (здесь n=5):

n = int(input())
i = 0
j = -1
max_j = n - 1 
max_i = n - 1
min_j = 0
min_i = 1
count = 1
mtrx = [[0 for j in range(n)] for i in range(n)]
while True:
    while j < max_j:
        j += 1
        mtrx[i][j] = count
        count += 1
    max_j -= 1
    while i < max_i:
        i += 1
        mtrx[i][j] = count
        count += 1
    max_i -= 1
    while j > min_j:
        j -= 1
        mtrx[i][j] = count
        count += 1
    min_j += 1
    while i > min_i:
        i -= 1
        mtrx[i][j] = count
        count += 1
    min_i += 1
    
    if j == (n - 1) // 2 and i == n // 2:
        break  
print()
print()
for i in range(n):
    for j in range(n):
        print(mtrx[i][j], end = ' ')
    print()

    