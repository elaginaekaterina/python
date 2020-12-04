genome = 'ATGG'
genome[0] = A
genome[1] = T
genome[2] = G
genome[3] = G

genome[-1] = G # 1 символ с конца
genome[-2] = G
genome[-3] = T
genome[-4] = A

i = 1 # индексация с помощью переменной
print(genome[i])

#Строки не изменяются
genome = 'ATGG'
genome[1]='C' # ошибка

#Перечисление символов строки с помощью инжексов
genome = 'ATGG'
for i in range(4):
    print(genome[i])

# Лучше использовать данное перечисление:
#Цикл for можно использовать для поочередного перечисления
#всех символов стороки
genome = 'ATTG'
for c in genome:# c принимает все значения строки genome
        print(c)

#Задача - цитозин
#Дана геномная последовательность.
#Вывести, сколько раз в ей встречается нуклеоид цитозин.
# 1 Вариант решения
genome = input()
cnt = 0 #счетчик
for nucl in genome:
    if nucl == 'C':
        cnt += 1
print(cnt)

# 2 Вариант решения
genome = input()
print(genome.count('C'))

#Строки имеют методы
#- ф-ия, которая применяется к данной строке
#- s.count(p) - сколько раз строка p встречается в строке s

#Некоторые методы у строк
s = 'aTGcc' p = 'cc'
- s.upper() ->'ATGCC'
- s.lower() ->'atgcc'
- s.count(p) -> 1 #сколько раз p встречается в s
- s.find(p) -> 3 #первое вхождение (индекс)p в s
- s.find('A') -> -1 #строка 'A' не входит в s
#Проверка вхождения в строку: if 'TG' in s: ...
- s.replace('c', 'C') -> 'aTGCC' #заменяем все вхождения 'c' на 'C'

# Последовательные вызовы методов
s = 'agTtcAGtc'
s.upper().count('gt'.upper())


#Напишите программу, которая вычисляет процентное содержание
#символов G (гуанин) и C (цитозин) в введенной строке
#(программа не должна зависеть от регистра вводимых символов)

#1 Вариант зависит от регистра вводимых символов
genome = input()
cnt = 0
pers = 0
for gc in genome:
    if gc == 'g' or gc == 'c':
        cnt += 1
        pers = (cnt/len(genome))* 100
print(pers)
        
#2 Вариант не зависит от регистра вводимых символов
genome = input()
Gcnt = genome.upper().count('g'.upper())
Ccnt = genome.upper().count('c'.upper())
GCcnt = Gcnt + Ccnt
pers = (GCcnt/len(genome))*100
print(pers)


#Slicing - Взятие диапазонов символов
dna = 'ATTCGGAGCT'
dna[1] -> 'T'
dna[1:4] -> 'TTC'
dna[:4] -> 'ATTC'
dna[4:] -> 'GGAGCT'
dna[-4:] -> 'AGCT'
dna[1:-1] -> 'TTCGAGC'
dna[1:-1:2] -> 'TCGG' #[start_ind,end_ind,step]
dna[::-1] -> 'TCGAGGCTTA' # символы в обратном порядке

# Задача - палиндром
# Дана геномная последовательность
# Проверить, явдяется ли она палиндромом
#(читается в обоих направлениях одинаково)
# 1 Способ
s = input()
i = 0
j = len(s)-1
is_palindrom = True
while i < j:
    if s[i] != s[j]:
        is_palindrom = False # после можно добавть break
    i += 1
    j -= 1
if is_palindrome:
    print('YES')
else:
    print('NO')

# 2 Способ; недостаток: требует мого памяти
s = input()
r = s[::-1]
if s == r:
    print('YES')
else:
    print('NO')

'''Осуществить кодирование следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
Напишите программу, которая считывает строку,
кодирует и выводит закодированную последовательность
Кодирование должно учитывать регистр символов.'''

s = str(input())
l = len(s) - 1
c = 1
kod = ''
if len(s) == 1:
    kod = kod + s + str(c)
else:
    for i in range(0,l):
        if s[i] == s[i + 1]:
            c += 1
        elif s[i] != s[i + 1]:
            kod = kod + s[i] + str(c)
            c = 1
    for j in range(l,l + 1):
        if s[-1] == s[-2]:
            kod = kod + s[j] + str(c)
        elif s[-1] != s[-2]:
            kod = kod + s[j] + str(c)
            c = 1
print(kod)
