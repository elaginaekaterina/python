students = ['Ivan', 'Masha', 'Sasha']
for student in students:
    print('Hello,' + student + '!')
# Доступ происходит с помощью инднксов
students = ['Ivan', 'Masha', 'Sasha']
#Длина списка: len(students)
# Доступ к эл.списка осуществляется как и к строкам
#так же берем и отрицательные индексы
students[-1] 'Sasha'
students[-2] 'Masha'
students[-3] 'Ivan'

#Опрерации со списками
+
students = ['Ivan', 'Masha', 'Sasha']
teachers = ['Oleg', 'Alex']
students + teachers
Результат: ['Ivan', 'Masha', 'Sasha','Oleg', 'Alex']
*
[0,1]*4
Результат: [0,1,0,1,0,1,0,1]

# Изменение списков
#В отличчии от изученных типов данных
(int, float, str) списки (list) являются ИЗМЕНЯЕМЫМИ
#Изменение конкретного элемента списка
students = ['Ivan', 'Masha', 'Sasha']
students[1] = 'Oleg'
print(students)
#Результат: ['Ivan', 'Oleg', 'Sasha']

#Добавление элемента списка
students = ['Ivan', 'Masha', 'Sasha']
students.append('Olga')
#Результат: ['Ivan', 'Masha', 'Sasha', 'Olga']
students += ['Olga']
#Результат: ['Ivan', 'Masha', 'Sasha', 'Olga', 'Olga']
students += ['Boris', 'Sergey']
#Результат: ['Ivan', 'Masha', 'Sasha', 'Olga', 'Olga','Boris', 'Sergey']
#Пустой список:
students = []
# Вставка элементов списка
students = ['Ivan', 'Masha', 'Sasha']
students.insert(1,'Olga')
#Результат: ['Ivan', 'Olga', 'Masha', 'Sasha']

students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)
#Результат: ['Ivan', 'Masha', 'Sasha', 'Olga', 'O', 'l', 'g', 'a']

#Удаление элемента из списка
students = ['Ivan', 'Masha', 'Sasha']
students.remove('Sasha')
#или
del students[0]

#Поиск элемента в списке
# 1 способ
students = ['Ivan', 'Masha', 'Sasha']
if 'Ivan' in students:
    print('Ivan is here')
if 'Ann' not in students:
    print('Ann is out')

# 2 способ
ind = students.index('Sasha')
#Результат: 2
ind = students.index('Ann')
#Результат: ValueError: 'Ann' is not in list

#Сортировка списка
# 1 Способ не меняет сам список
students = ['Sasha','Ivan', 'Masha']
ordered_students = sorted(students)
#Результат: ['Ivan', 'Masha', 'Sasha']

# 2 способ меняет сам список
students.sort()
#Результат: ['Ivan', 'Masha', 'Sasha']

#Если не нужно сортировать весь список, а нужно только получить
#самого первого или самого последнего используем (элементы должны быть сравнимы)
min()
max()

# Список в обратном порядке(Изменяет сам список)
students = ['Sasha','Ivan', 'Masha']
students.reverse()
#Результат: ['Masha', 'Ivan', 'Sasha']

# не изменяют сам список:
reversed(students) 
stidents[::-1]

# Присвоение списков
a = [1, 'A', 2]
b = a
a[0] = 42
#Значение a: [42, 'A', 2]
#Значение b: [42, 'A', 2]
b[2] = 30
#Значение b: [42, 'A', 30]
#Значение a: [42, 'A', 30]


# Генерация списков
a = [0]*5
a = [0 for i in range(5)]
a = [i * i for i in range(5)] 
a = [int(i) for i in input().split()] #split - делит строку по пробелам

#Напишите программу, на вход которой подается одна строка с целыми числами.
#Программа должна вывести сумму этих чисел.
a = [int(i) for i in input().split()]
print(sum(a))


На вход подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка.
Если на вход пришло только одно число, надо вывести его же.
Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

a = [int(i) for i in input().split()]
l = len(a)- 1
s = 0
nov = []
i = 0
if len(a) == 0:
    print(str(0))
else:
    for ai in a:
        if len(a) > 1:
            if i == 0:
                s = a[i+1] + a[-1]
                nov.append(s)
            elif i > 0 and i < l:
                s = a[i-1] + a[i+1]
                nov.append(s)
            elif i == l:
                s = a[i-1] + a[0]
                nov.append(s)
        elif len(a) == 1:
            s = a[i]
            nov.append(s)
        i += 1
    j = 0
    for ai2 in nov:
        print(str(nov[j])+' ', end='')
        j += 1


На вход подается список чисел в одной строке, вывод в
одну строку повторяющихся более одного раза значений.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

s = [ int(i) for i in input().split()]
nov = []
s.sort()
l = len(s)-1
k = 100000
if len(s)!=1:
    for i in range(0,l):
        if s[i] == s[i+1] and s[i] != k:
            nov.append(s[i])
            k = s[i]
    for j in range(l,l+1):
        if s[-1] == s[-2] and s[j] != k:
            nov.append(s[j])
n = len(nov)
for g in range(0,n):
    print(nov[g],end=' ')


# Генерация двумерных списков
a = [[1,2,3],[4,5,6],[7,8,9]]
     a[1] -> [4,5,6]
     a[1][1] -> 5

# Инициализация дум.списков
n = 3
a = [[0]*n]*n
a[0][0] = 5 #в первом стобце все элементы 5
# Зависимый список поскольку создали строку из n нулей и скопировали ссылку на нее n раз

#Создание n списков из n нулей, где каждый список будет независимый
a = [[0] * n for i in range(n)]
a =[[0 for j in range(n)] for i in range(n)]
