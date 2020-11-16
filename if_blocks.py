# Условия: if, else, elif. Блоки, отступы
#if x % 2 == 0:
#    print('Четное')
#else:
#    print('Нечетное')


# Найти наибльшее из 2-ух чисел
#a = 4
#b = 7
#if a >= b:
#    print(a)
#else :
#    print(b)

# второй вариант может применяться для произв числа чисел
#a = 4
#b = 7
#m = a
#if b > m:
#    m = b
#print(m)

#a = int(input())
#b = int(input())
#if b != 0:
#    print(a / b)
#else:
#    print('Деление невозможно')
#    b = int(input('Введите ненудевое значение'))
#    if b == 0:
#        print('Вы не справились!')
 #   else:
  #      print(a / b)

# Задача про Аню
#A = int(input())
#B = int(input())
#H = int(input())
#if  H >= A and H <= B:
 #   print('Это нормально')
#elif H < A:
 #   print('Недосып')
#elif H >= B:
   # print('Пересып')

# Високосный год
n = int(input())
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('Висоскосный')
else:
    print('Обычный')
