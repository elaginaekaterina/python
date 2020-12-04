'''
Напишите программу, которая принимает на стандартный вход список
игр футбольных команд с результатом матча и выводит на стандартный
вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.


n = int(input())
x = [input().split(';') for x in range(n)]
vs = [(x[0], x[2]) for x in x]
import itertools
clubs = set(itertools.chain.from_iterable(vs))
res = {club:[0, 0, 0, 0, 0] for club in clubs}
for team1, gol1, team2, gol2 in x:
    res[team1][0] += 1
    res[team2][0] += 1
    if int(gol1) > int(gol2):
        res[team1][1] += 1
        res[team1][4] += 3
        res[team2][3] += 1
    elif int(gol1) < int(gol2):
        res[team2][1] += 1
        res[team2][4] += 3
        res[team1][3] += 1
    elif int(gol1) == int(gol2):
        res[team1][2] += 1
        res[team1][4] += 1
        res[team2][2] += 1
        res[team2][4] += 1
for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, res[club]))))



Напишите программу, которая умеет шифровать и расшифровывать шифр
подстановки. Программа принимает на вход две строки одинаковой длины,
на первой строке записаны символы исходного алфавита, на второй строке —
символы конечного алфавита, после чего идёт строка, которую нужно зашифровать
переданным ключом, и ещё одна строка, которую нужно расшифровать.


s=str(input())
a=[]#строка, которую необходимо зашифровать
for i in range(len(s)):
    si=s[i]
    a.append(si)
b=[]
n=str(input())
for j in range(len(n)):
    sj=n[j]
    b.append(sj) #print(b)
p={} #инициализация словаря
for pi in range(len(s)):
    key=s[pi]
    p[key]=0
j1=0
for i in range(0,len(a)):
    key=a[i]
    while j1<len(b):
        bj=b[0]
        if key in p:
            p[key]=bj
        b.remove(bj)
        break
c=[]
si=str(input())
for si1 in range(0,len(si)):
    ci=si[si1]
    c.append(ci)
co=[]
for ci in range(0,len(c)):
    if c[ci] in p:
        cco=c[ci]
        pco=p[cco]
        co.append(pco)
d=[]
di=str(input())
for sj1 in range(0,len(di)):
    dj=di[sj1]
    d.append(dj)
do=[]
for di in range(0,len(d)):
    for key in p:
        pkey=key
        if p.get(key) == d[di]:
            ddo=pkey
            do.append(ddo)
for i in range (0,len(co)):
    print(co[i],end='')
print()
for j in range (0,len(do)):
    print(do[j],end='')



На вход программе первой строкой передаётся количество d известных нам слов,
после чего на d строках указываются эти слова. Затем передаётся количество l
строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке.
Работу производите без учёта регистра.


a = int(input())
b = []
for i in range(a):
    x = input().lower()
    if x not in b:
        b.append(x)
 
d = int(input())
e = []
for j in range(d):
    x = input().lower().split()
    for i in x:
        if i not in b and i not in e:
            e.append(i)
            
print('\n'.join(e))



Программе подаётся на вход число команд nn, которые нужно выполнить черепашке,
после чего nn строк с самими командами. Вывести нужно два числа в одну строку:
первую и вторую координату конечной точки черепашки.
Все координаты целочисленные.

commands_sum = {'север': 0, 'юг': 0,
                'запад': 0, 'восток': 0}

for command, value in [input().split() for _ in range(int(input()))]:
    commands_sum[command] += int(value)

print(commands_sum['восток'] - commands_sum['запад'],
      commands_sum['север'] - commands_sum['юг'])
'''


with open('dataset7.txt', 'r') as f, open('outdataset7.txt', 'w') as g:
    s = []
    v = 0
    for line in f:
        s += line.split()
        v += 1
 
    t = [0] * 11
    t2 = [0] * 11
    k = 0
    for i in range(2, v * 3, 3):
        k = int(s[i - 2])
        if 1 <= k <= 11:
            t[k - 1] += int(s[i])
            t2[k - 1] += 1
 
    for i in range(0, 11):
        value = [i + 1, ' ', t[i] / t2[i], '\n']
        for x in value:
            g.write(str(x))
