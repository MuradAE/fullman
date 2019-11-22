# 9 Урок Операции со строками

# s = 'C:d\new.txt'
# print (s)               #C:d --- #ew.txt


# s = 'C:\d\\new.txt'
# print (s)               #C:d\new.txt


# s = r'C:\d\new.txt'
# print (s)               #C:\d\new.txt
# r - Raw string (Сырая строка)

                  
'''конкатенация строк -  
операция склеивания объектов линейной структуры, обычно строк'''

# s = 'Py' 'thon'
# print (s)                 #Python

# s1 = 'Hello, '              #переменная s1 
# s2 = 'world'                #переменная s2
# s3 = s1 + s2 # (+) конкатенация строк (Сложение строк)
# print (s3)   # Hello, world

# name = 'Murad'
# age = 20
# print ('My name is ' + name) #My name is Murad

# name = 'Murad'
# age = 20
# print ('My name is ' + name + " i'm " + str (age)) #My name is Murad i'm 2


#Повторение строк 
# print ('me me me me me')  #me me me me me
# print ('me ' * 5)         #me me me me me


'''Индексация и срез строк в Python 3. Строки – это тип данных Python,
 который представляет собой последовательность из одного или нескольких 
 символов'''

# s = 'Hello world!'
# print (s[0])                #H (1й символ)

# s = 'Hello world!'
# print (s[11])               #! (11 символ)

# s = 'Hello world!'
# print (s[-2])               #d (10 символ обратный счет!)

'''
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9   10  11  12
-12-11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1  -0
'''
# s= ('Hello world!')
# print (s[0:12])                #Hello world!

s= ('Hello world!')
print (s[0:5])   #Hello

s= ('Hello world!')
print (s[:5])    #Hello

s= ('Hello world!')
print (s[6:])    #world!

s= ('Hello world!')
print (s[::2])   #Hlowrd

s= ('Hello world!')
print (s[::-1])  #dlrow olleH (перевернуть строку)

s= ('Hello world!')
print (s[:5] + s [6:])  #Helloworld!