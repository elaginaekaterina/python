# Чтение из файла
inf = open('file.txt', 'r') # open('file.txt'), 'r' - параметр указывающий, что открываем для чтения
s1 = inf.readline() # readline - чтение 1-ой строки
s2 = inf.readline()
inf.close # закрытие файла


# Конструкция для чтения из файла, закрытие файла уже предусмотрено
with open('text.txt') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

# Функции
s = inf.readline().strip() # strip() - убирает все служебные символы строки
'\t abs   \n'.strip() -> 'abs'

# Чтобы воспользоваться этой ф-ей надо подключить модуль os
os.path.join('.', 'dirname', 'filename.txt') # построить полный путь к файлу для любой ОС
'./dirname/filename.txt'


#Построчное чтение файла
with open('input.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)

# Запись в файл
ouf = open('file.txt', 'w') # 'w' - запись в файл
ouf.write('Some text\n')
ouf.write(str(25))
ouf.close()

# Конструкция для записи в файл, закрытие файла уже предусмотрено
with open('text.txt', 'w') as ouf:
    ouf.write('Some text\n')
    ouf.write(str(25))



#1.
#Напишите программу, которая считывает из файла строку, соответствующую тексту,
#сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
#Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
#В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

with open ('dataset2.txt','r') as (e):
    s1 = e.readline()
f = 0
n = ''
l = []
for i in range (len(s1)):
    # print (s1[i])
    if s1[i].isdigit():
        n += s1[i]
    elif s1[i].isalpha():
        if i >= 1:
            n1 = int(n)
            l.append(n1)
            n = ''
        l.append(s1[i])
if len(n) > 0:
    l.append(int(n))
n = ''
for i in range (0,len(l),2):
    n += (l[i]*l[i+1])
with open ('answers.txt','w') as (e):
    e.write(n)
 

#2.
#Напишите программу, которая считывает текст из файла
#(в файле может быть больше одной строки) и выводит самое частое слово
#в этом тексте и через пробел то, сколько раз оно встретилось.
#В качестве ответа укажите вывод программы, а не саму программу.
#Слова, написанные в разных регистрах, считаются одинаковыми.

dict = {}

with open('dataset3.txt') as in_f:
	for line in in_f:
		line = line.lower()
		for word in line.split():
			if word not in dict:
				dict[word] = 1
			elif word in dict:
				dict[word] += 1			

maxq = 1
	
for key, value in dict.items():
	current_q = dictionary[key]
	if current_q > max_q:
		max_q = current_q
		word_with_max_q = key
	
with open('answer_dataset3.txt', 'w') as out_f:
	most_popular = (word_with_max_q+ ' ' + str(max_q))
	out_f.write(most_popular)

#3.
#Имеется файл с данными по успеваемости абитуриентов.
#Он представляет из себя набор строк, где в каждой строке
#записана следующая информация:
#Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#Напишите программу, которая считывает исходный файл с подобной структурой и
#для каждого абитуриента записывает его среднюю оценку по трём предметам на
#отдельной строке.

#Также вычислите средние баллы по математике, физике и русскому языку по
#всем абитуриентам и добавьте полученные значения, разделённые пробелом,
#последней строкой в файл с ответом.

math = []
physics = []
russian = []
with open('dataset4.txt', 'r') as in_f:
    for line in in_f:
        current_line = line.strip().split(';')
        math.append(int(current_line[1]))
        physics.append(int(current_line[2]))
        russian.append(int(current_line[3]))
out_f = open('answer_dataset4.txt', 'w')
for i in range(len(math)):
    out_f.write(str((math[i] + physics[i] + russian[i]) / 3) + '\n')
if len(math) > 0:
    out_f.write(str(sum(math) / len(math)) + ' ' +
                   str(sum(physics) / len(physics)) + ' ' +
                   str(sum(russian) / len(russian)))
out_f.close()
	
