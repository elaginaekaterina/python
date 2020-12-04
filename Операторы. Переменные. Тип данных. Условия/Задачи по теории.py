'''
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c)/2
s = (p * (p - a) * (p - b) * (p - c))**0.5
print(float(s))
'''

'''
a = int(input())
if -15 < a <= 12 or 14 < a < 17 or 19 <= a < float("inf"):
    print(True)
else:
    print(False)
'''

'''
a = float(input())
b = float(input())
c = str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == "*":
    print(a * b)
elif c == 'mod' and b != 0:
    print(a % b)
elif c == 'mod' and b == 0:
    print('Деление на 0!')
elif c == '/' and b != 0:
    print(a / b)
elif c == '/' and b == 0:
    print('Деление на 0!')
elif c == 'div' and b != 0:
    print(a // b)
elif c == 'div' and b == 0:
    print('Деление на 0!')
elif c == 'pow':
    print(a ** b)
'''

'''
pi = 3.14
fig = str(input())
if fig == 'прямоугольник':
    a = float(input())
    b = float(input())
    s1 = a * b
    print(s1)
elif fig == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c)/2
    s2 = (p *(p - a)*(p - b)*(p - c))**0.5
    print(s2)
elif fig == 'круг':
    r = float(input())
    s3 = pi * r**2
    print(s3)
'''


'''
x = int(input())
y = int(input())
z = int(input())
if x > y and x > z:
    max = x
    if y > z:
        mid = y
        min = z
    else:
        mid = z
        min = y
    print(max,'\n',min,'\n',mid,'\n')
elif y > x and y > z:
    max = y
    if x > z:
        mid = x
        min = z
    else:
        mid = z
        min = x
    print(max,'\n',min,'\n',mid,'\n')
elif z > x and z > y:
    max = z
    if x > y:
        mid = x
        min = y
    else:
        mid = y
        min = x
    print(max,'\n',min,'\n',mid,'\n')    
elif z == x and y == z:
    max = x
    min = y
    mid = z
    print(max,'\n',min,'\n',mid,'\n')  
elif z == x and (y > x or y > z):
    max = y
    min = z
    mid = x
    print(max,'\n',min,'\n',mid,'\n') 
elif z == x and (y < x or y < z):
    max = x
    min = y
    mid = z
    print(max,'\n',min,'\n',mid,'\n') 
elif x == y and (z < y or z < x):
    max = x
    min = z
    mid = y
    print(max,'\n',min,'\n',mid,'\n')
elif x == y and (z > b or z > x):
    max = x
    min = y
    mid = z
    print(max,'\n',min,'\n',mid,'\n')
elif z == y and (x > z or x > y):
    max = x
    min = z
    mid = y
    print(max,'\n',min,'\n',mid,'\n')
elif z == y and (x < z or x < y):
    max = z
    min = x
    mid = y
    print(max,'\n',min,'\n',mid,'\n')
'''

'''
n = int(input())
if  n>=0:
  if n==0:
    print(n, 'программистов')
  elif n%100>=10 and n%100<=20:
    print(n, 'программистов')
  elif n%10==1:
    print(n, 'программист')
  elif n%10>=2 and n%10<=4:
    print(n, 'программиста')
  else:
    print(n, 'программистов')
'''


s = int(input())
s1 = s % 10
s = s // 10
s2 = s % 10
s = s // 10
s3 = s % 10
s = s // 10
s4 = s % 10
s = s // 10
s5 = s % 10
s = s // 10
s6 = s % 10
if s6 + s5 + s4 == s3 + s2 + s1:
    print('Счастливый')
else:
    print('Обычный')
