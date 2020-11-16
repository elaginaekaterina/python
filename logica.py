# Логические значения
# false(0) true(1)
# Операции x or y, x and y, not x

# Операции сравнения
# < строго меньше
# <= меньше или равно
# > сторого больше
# >= больше или равно
# == равно
# != не равно


# Практика
#a = int(input())
#print(a > 0)

#a = int(input())
#print(a >= 10 and a < 100)
#the same
#a = int(input())
#print(10 <= a < 100)


#x1, x2, x3 = False, True, False
#not x1 or x2 and x3 # первой not -> and -> or
#((not x1) or x2) and x3 # скобки задают преоритет


#x = 5
#y = 10
#print(y > x * x or y >= 2 * x and x < y)

a = True
b = False
print(a and b or not a and not b)
