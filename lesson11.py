''' Форматирование строк

'''

name = 'John'
age = 34
# print('My name is ' + name + '. I\'m ' + str(age ))
# print('My name is  % (name)s. I\'m  %(age)d' %{'name': name, 'age': age}) #не работает!!!
#print('My name is  %s. I\'m  %d' % ('David', age))
print('Title: %s, Price: %f' %('Sony', 40)) #Title: Sony, Price: 40.000000
print('Title: %s, Price: %.2f' %('Sony', 40)) #Title: Sony, Price: 40.00

# format 
# print ('My name is {}. I\'m {}'.format(name, age))
# print ('My name is {0}. I\'m {1}'.format(name, age))
# print ('My {1} name is {0}. I\'m {1}'.format(name, age))

# f-strings
# print (f'My name is {name}. I\'m {age}')
print (f'My name is {name}. I\'m {age + 5}')
print('5 + 2 = {}'. format (5 + 2))
print(f'5 + 2 - {5 + 2}')



