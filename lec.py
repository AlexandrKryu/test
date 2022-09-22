# value = None

# print(type(a))
# print(type(b))
# print(type(value))
# s = "Hello World"  # \n -Это перенос строки ниже
# a = 123
# b = 1.25

# Что и как будем выводить

# print(a, "-", b, "-", s)  # знаки между данными в '-'
# print("{} - {} - {}".format(a, b, s))  # тоже самое что и на 9й
# print("{2} - {0} - {1}".format(a, b, s))  # цифры определяют порядок вывода
# print(f"{a} - {b} - {s}"
# )  # недавно появилась функция прямо в скобках с назначением f интерполяция
# f = True # True или False правда и лож Запомнить
# print(f)
# list = [1, "Hello", True]  #списки, можно сразу все миксовать
# # но этого лучше не делать(те используется динамическая типизация)
# print(list)

# print("введите а")
# a = int(input())
# print("введите b")
# b = int(input())    #чтоб было числовым значением добавим int если строка то без него
# print(f"{a} + {b} = {a+b}")


#                           Арифметические операции
# + ,- ,* ,/ ,% ,// , **

# a = 1.3
# b = 4
# c = round( a * b, 3)  # раунд округляет а после последней запятой выбираем количество чисел после запятой
# print(c)

#                               Логические
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, in not
# gen

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f)  #ищем 2 в списке f или исключаем этим (not 2 in f)

#                   Хрень с if и if-else      нужны отступы

# a = (input("a = "))  # уороченый ввод с пояснениме
# b = (input("b = "))
# if a > b:
#     print(a)
# else:
#     print(b)
#  if и elif  логическая нечто
# username = input('Введите имя: ')
# if username=='Маша':
#     print('Ура, этоже Маша!')
# elif username =='Тарзан':
#     print('ООО Никита когда долг отдаш?')
# elif username == 'Ильнар':
#     print('О Ильнар красавчеГ')
# else:
#     print('Трям', username)

# original = 95
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10                     #не забывать про равенство по действию!
# else:
#     print("Все харэ!")
# print(inverted)

#                           Управляющие конструкии for

# list = [1,3,5,7,8,9]
# for i in list:
#     print(i**3)

# for i in range(1, 10, 2):  # последняя цифра указывает на сколько будет менятся i
#     print(i)

# for i in 'Чарон':
#     print(i)

# help(format)  - подсказка по непонятным наборам букв от Питона

#                               Списки
# ram = range(2, 7) # определяем для начала длину
# print(type(ram))
# numbers = list(ram) # создаем список с заданной длиной
# print(type(numbers))

#                           Расширеный функционал

colors =['red','green','blue']

for i in colors:
    print(i)

for i in colors:
    print(i*2)

colors.append('grey')  #что то добавляем в конец списка
print(colors)
# colors.remove('red') # что то выпииваем из списка или del colors[2]
print(colors)

#                       Функции аля Методы


# def f(x):
#     if x == 1:
#         return "Целое"
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 1
# print(f(arg))
# print(type(f(arg)))