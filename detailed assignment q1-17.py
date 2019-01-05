PRACTICE PROBLEM 3.1
a)
age = eval(input('Enter your age:'))
if age > 62:
    print('You can get your pension benefits')


b)
name = (input('Enter the name of any baseball player name:'))
if name in ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']:
    print('One of the top 5 baseball players,ever!')


c)
hit = eval(input('Enter the number of hits:'))
shield = eval(input('Enter the number of shields:'))
if hit > 10 and shield == 0:
    print('You are dead...')


d)
variable = eval(input('Enter the direction of boolean variables:'))
north = 8
west = 9
south = 6
east = 4
if north or south or west or east == true:
    print('I can escape.')
    

PRACTICE PROBLEM 3.3
a)
year = eval(input('Enter the year:'))
if year%4==0 and (year%100!=0 or year%400==0):
    print('Could be a leap year')
else:
    print('Definitely not a leap year')

    
b)
LT = eval(input('Enter the ticket number:'))
LL = eval(input('Enter the lottery number:'))
if LT == LL:
    print('You won!')
else:
    print('Better luck next time...')


PRACTICE PROBLEM 3.4

User = input('Enter your login ID:')
list = ['joe', 'sue', 'hani', 'sophie']
if User in list:
    print('You are welcome!')
else:
    print('Unknown user')
print('Done.') 


PRACTICE PROBLEM 3.5

word =  ['stop', 'desktop', 'top', 'post']
for words in word:
    if len(words) == 4:
        print(words)


PRACTICE PROBLEM 3.6
a)
for number in range(10):
    print(number)


b)
for number in range(10):
    print(number)


PRACTICE PROBLEM 3.7
a)
for number in range(3,13):
    print(number)


b)
for number in range(0,9,2):
    print(number)


c)
for number in range(0,24,3):
    print(number)


d)
for number in range(3,12,5):
    print(number)

PRACTICE PROBLEM 3.8
def perimeter(r):
    n = 2*3.142*r
    return(n)
b = perimeter(1)
b2 = perimeter(2)
print(b)
print(b2)

PRACTICE PROBLEM 3.9
def average(x, y):
    return(x+y)/2
A = average(1,3)
print(A)
B = average(2,3.5)
print(B)

PRACTICE PROBLEM 3.10
def novowel(x):
    for i in x:
        if i in "aeiouAEIOU":
            return False
    return True
v = noVowel('python')
print(v)

PRACTICE PROBLEM 3.11
def allEven(x):
    for num in x:
        if num % 2 != 0:
            return False
    return True
numbers = allEven([3,2,-8,-7,10])
print(numbers)

PRACTICE PROBLEM 3.12
def negatives(number):
    neg_num = []
    for i in number:
        if i < 0:
            neg_num.append(i)
    return neg_num

x = negatives([1,3,-9,-10,-6,-8])
print(*x, sep ="\n")

PRACTICE PROBLEM 3.13
def average(x, y):
    return(x+y)/2
    
help(average)


def negatives(number):
    neg_num = []
    for i in number:
        if i < 0:
            neg_num.append(i)
    return neg_num

help(negatives)

PRACTICE PROBLEM 3.17
a = eval('2*3+1')
print(a)

b = eval('hello')
print(b)
#it will give error because hello in not defined
"""Traceback (most recent call last):
  File "C:/Users/hp/Desktop/3.17.py", line 4, in <module>
    b = eval('hello')
  File "<string>", line 1, in <module>
NameError: name 'hello' is not defined"""
c = eval("'hello' + ' ' + 'world!'")
print(c)

d = eval("'ASCII'.count('I')")
print(d)

e = eval('x = 5')
print(e)
#it will give error due to syntax error
"""Traceback (most recent call last):
  File "C:/Users/hp/Desktop/3.17d).py", line 1, in <module>
    e = eval('x = 5')
  File "<string>", line 1
    x = 5
      ^
SyntaxError: invalid syntax"""
