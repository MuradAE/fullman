#Методы строк
'''
len - Длина строки

str.capitalize - Переводит первый симвал строки в верхний регистр, 
а все остольные в нижний

str.center(width),[fill] - Возвращает отцентрованную строку, по краям 
который стоит символ fill (пробел по умолчанию)

str.count(str, (start),(end)) - Возвращает количество непересекающихся 
вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)

str.find(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1

str.index(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError

str.replace (шаблон, замена) - Замена шаблона

str.split ([символ]) - Разбиение строки по разделителю

str.isdigit() - Состоит ли строка из цифр
str.isalpha() - Состоит ли строка из букв
str.isalnum() - Состоит ли строка из цифр или букв
str.islower() - Состоит ли строка из символов в нижнем регистре
str.isupper() - Состоит ли строка из символов в верхнем регистре



'''
s = 'hello'
# print(len(s))           #5

# print(s.capitalize())   # Hello
# s2 = s.capitalize()
# print(s, s2)            #hello Hello

# print(s.center(20))       #       hello
# print(s.center(20, '!'))    #!!!!!!!hello!!!!!!!!

# print(s.count('h')) #1
# print(s.count('e')) #1
# print(s.count('l')) #2
# print(s.count('o')) #1

# print(s.find ('h')) #0
# print(s.find ('e')) #1
# print(s.find ('l')) #2
# print(s.find ('l')) #3
# print(s.find ('o')) #4

# print(s.index ('o'))  #4
# print(s.index ('a'))  #то выводит ошибку

# print (s.replace('l', 't')) #hetto

#-----------------#
s3 = 'hello, world'
# print(s3.split(','))

# print (s3.isdigit())
# print(s3.isalpha())