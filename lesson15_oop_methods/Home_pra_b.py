# Сделать класс Printer с полем
# кол-во чб чернил
# кол-во цветных чернил

# и методом
# printFile(isColor, pagesCount) - isColor - цветная перчать или чб, pagesCount - кол-во страниц для печати
# Метод должен оценить кол-во чернил в принтере, если хватит, то распечатать
# на каждую страницу уходит по 5 чернил

# class Printer:
#
#     def __init__(self, b_w_ch, color_ch):
#         self.b_w_ch = b_w_ch
#         self.color_ch = color_ch
#
#     def printFile(self, isColor, pagesCount):
#         need_chern = pagesCount * 5
#         if isColor:
#             if self.color_ch >= need_chern:
#                 print('Прошла цветная печать')
#                 self.color_ch -= need_chern
#             else:
#                 print('не хватает цветных чернил')
#
#         else:
#             if self.b_w_ch >= need_chern:
#                 print('Черно-белая печать')
#                 self.b_w_ch -= need_chern
#             else:
#                 print('Черно-белых чернил не хватает')
#
# printer = Printer(10, 20)
# printer.printFile(True, 2)
# printer.printFile(True, 2)
# printer.printFile(True, 2)
# printer.printFile(False, 2c)


# Сделать класс Tv - телевизор  с полями
# марка
# текущий канал

# Сделать класс Remote с полями
# tv - телевизор
# и методы:
# next_channel()
# prev_channel()
# Пульт может управлять разными телевизорами

# class Tv:
#
#     def __init__(self, marka, kanal):
#         self.marka = marka
#         self.kanal = kanal
#
#     def printCurrentChanal(self):
#         print('У телевизора {}, текущий канал {} '.format(self.marka, self.kanal))
#
# class Remote:
#     tv = None
#
#     def next_chanal(self):
#         print('Включаем следующий канал ', self.tv.marka)
#         self.tv.kanal += 1
#
#     def prev_chanal(self):
#         print('Включаем предыдущий канал', self.tv.marka)
#         self.tv.kanal -= 1
#
# tv1 = Tv('lg', 1)
# tv2 = Tv('lgs', 2)
#
# remote = Remote()
# remote.tv = tv1
# remote.next_chanal()
# remote.tv.printCurrentChanal()
# remote.next_chanal()
# remote.tv.printCurrentChanal()
#
# remote.tv = tv2
# remote.next_chanal()
# remote.tv.printCurrentChanal()
# remote.next_chanal()
# remote.tv.printCurrentChanal()



# Создать класс Аккаунт с полями: login, password, name, history (исптория входа в аккаунт)
# history это строка, ктороая содержит название устройства, с которого был выполнен последний вход в аккаунт
# Сделать метод смены пароля (метод принимает в качестве занчения параметр - новый пароль)

# class Accaunt:
#
#     def __init__(self, login, password, name, history):
#         self.login = login
#         self.password = password
#         self.name = name
#         self.history = history
#
#     def changePass(self, newPassword):
#         self.password = newPassword
#
# acc_list = [Accaunt("Jopa", '123', 'GankBank', 'Yota'), Accaunt('Popa', '123q', 'Igor', 'Nokia'), Accaunt('Uopa', '123w', 'OBama', 'Govno'), Accaunt('Hopa', '123e', 'HarryPotter', 'Sova2')]
#
# userInput = 0
#
# accIndex = -1
#
# while userInput != 6:
#     print('1 Вход')
#     print('2 Смена пароля')
#     print('3 Проверить на взлом')
#     print('4 Вывести устройство')
#     print('5 Выйти из аккаунта')
#     print("6 Выход")
#
#     userInput = int(input('Введи что хочешь : '))
#
#     if userInput == 1:
#         login = input('введи логин: ')
#         password = input('Пароль: ')
#         device = input('Устройство: ')
#         marker = False
#
#         for i in range(len(acc_list)):
#             if login == acc_list[i].login and password == acc_list[i].password:
#                 print('Вы вошла На ...')
#                 acc_list[i].history = device
#                 marker = True
#                 accIndex = i
#
#         if not marker:
#             print('Войти в аккаунт не удалось')
#
#     elif userInput == 2:
#         if accIndex == -1:
#             print('Войди в аккаунт ')
#         else:
#             newPassword = input('Введи новый пароль : ')
#             acc_list[accIndex].changePass(newPassword)
#             print('Пароль стал другим ')
#
#     elif userInput == 3:
#         if marker:
#             print('Последнее устройство было: ', acc_list[accIndex].history)
#             anser = input('твое устройство? ')
#             if anser == 'нет':
#                 print('Тебя взломали лол')
#         else:
#             print('Надо войти в аккаунт ')
#
#     elif userInput == 4:
#         if accIndex == -1:
#             print('Надо сперва войти')
#         else:
#             print('Вы входили с ', acc_list[accIndex].history)
#
#     elif userInput == 5:
#         if accIndex == -1:
#             print('Вы не входили ')
#         else:
#             accIndex = -1
#             print('Вышли из аккаунта')


# Задача 3 Запрограммируйте процесс совершения покупки между клиентом и магазином.
#
# Создайте класс Shop:
# class Shop:
#   balance //баланс магазина, изначально равен 0
#
#
#   //Создайте метод, который выводит price list магазина
#   def printPriceList():
#     print("яблоко - 20 руб")
#     print("апельсин - 25 руб")
#     print("банан - 30 руб")
#     print("груша - 15 руб")
#
#
#
#
# Создайте класс Client
# class Client:
#   balance //баланс клиента
#
#   //Создайте конструктор для инициализации поля balance
#
#   def buy(price):
#     //Метод должен проверять, что у клиента баланс позволяет купить покупку (неважно какую) по цене price
#     //и в случае успеха списывать деньги с баланса клиента
#     //метод должен возвращать true, если операция прошла успешно, иначе false
#
#
# Cоздайте объект Магазин (объект класса Shop) и клиента (объект класса Client).
# Напишите консольное меню:
# 1. Вывести доступные товары из магазины (метод PrintPriceList)
# 2. Купить товар (юзер вводит с консоли название и цену товара, у юзера вызывается метод buy, в который передается цена и магазин. в случае успеха метод вернет true и в мейне можно будет вывести, что товар такой-то был успешно куплен, после чего к балансу магазина нужно прибавить сумму проданного товара, либо не куплен)
# 3. Показать баланс магазина
# 4. Показать баланс покупателя
# 5. Выход