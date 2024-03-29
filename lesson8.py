#  Строки 

#' #строка объявляется в одинарных скобках.
#"" #либо двойных кавычках

words = 'Hello, world!'
print (words)

words = "Hello, world!"
print (words)

words = 'Hello, "world"!'
print (words)

words = "Hello, 'world'!"
print (words)

words = "Hello, \"test\" 'world'!"
print (words)
# \ Это экранирующий символ

words = "Hello, \test 'world'!"
print (words)
# \t Это экранирующая последовательность

words = "Hello, \\test 'world'!"
print (words)
# \t Это экранирующая последовательность

verse = 'Всё тихо — полная луна\
Блестит меж ветел над прудом,\
И возле берега волна\
С холодным резвится лучом.'
# \ экранирующий символ (говорим, что стих это одна логическая строка)
print (verse)

verse = 'Всё тихо — полная луна\n\
Блестит меж ветел над прудом,\n\
И возле берега волна\n\
С холодным резвится лучом.'
# \n\ экранирующий символ (перевод на новую строку)
print (verse)

verse = 'Всё тихо — полная луна\n' \
'Блестит меж ветел над прудом,'
print (verse)

verse = '''Всё тихо — полная луна
Блестит меж ветел над прудом,
И возле берега волнаS
С холодным резвится лучом
'''
print (verse)