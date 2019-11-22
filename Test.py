# box1 = 5
# box2 = 45
# box3 = box1 + box2
# print (box3)


# name = input ('Введите ваше имя:')
# name = 'Вас зовут: ' + name
# print (name)

# name = input ('Введите ваше имя:')
# age = input ('Введите сколько вам лет:')
# name = 'Вас зовут:' + name
# age = 'Вам:' + age + 'лет'
# print (name)
# print (age)

# a = 12
# b = 2 
# c = (a+b)*b
# print (c)

# a = input ('Введите сколько вам лет:')
# b = 100 - int (a)
# print ('Вам осталось жить где-то:' + str (b))

# sun = input ('Введите 1 если погода солнечная и 2 если пасмурная:')
# if (sun=='1'): d='Нужно загорать'
# else: d='Загорать не выйдет'
# print(d)

# myname = input('Ведите логин')
# mypass = input('Ведите пароль')
# if ((myname=='admin')and (mypass=='admin')): print ('Добро пожаловать, вы наш человек')
# else: print ('Ты хто такой, тавай дасвмдания...')

myname = input('Ведите логин')
mypass = input('Ведите пароль')
if (((myname=='Murad') and (mypass=='admin')) or ((myname=='Maga')and (mypass=='admin'))): 
    print ('Привет,'+myname + '. Добро пожаловать!')
else:
    print ('Ты хто такой тавай дасвидания')