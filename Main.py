import re
import os

'''
Naufal Husain Al-Thaariq
1152100032
IFA
'''

buyer = {}
seller = {}
catalogue = {}

class User:

    def __init__(self, name):
        self.__name = name
    pass

    def delUser(self, name):
        if name in buyer:
            del buyer[name]
        elif name in seller:
            del seller[name]
        else:
            print('User unavailable')

class Buyer(User):

    def __init__(self, name):
        super().__init__(name)
        self.__Basket = {}

    def basket(self, name):
        pass

class Seller(User):

    def __init__(self, name):
        super().__init__(name)
        self.__catalogue = {}
    pass

    def new(self, name, item):
        if name in self.__catalogue:
            catalogue[name].add(item)
        else:
            print('Catalogue Not found')

        pass

class Catalogue:

    def __init__(self, name):
        self.__name = name
        self.__item = {}
    
    def add(self, name):
        self.__item[name] = Item(name)
    pass

    def see(self):
        print(self.__name)
        if len(self.__item) != 0:
            for i in self.__item.values():
                print(i)


class Basket:

    def __init__(self, name):
        self.__name = name
        self.__item = []
    
    def add(self, item):
        self.__item.append(item)
    pass

while True:
    userInput = input('Input Commnad. for help \'?\'\n> ')
    userInput = re.split(',|, ', userInput)

    if userInput[0].lower() == 'buyer':
        Buyer(userInput[1].lower())
    elif userInput[0].lower() == 'seller':
        Seller(userInput[1].lower())
    elif userInput[0].lower() == 'catalogue':
        if userInput[0] in seller:
            Catalogue(userInput[1].lower())
        else:
            print('Unknown seller')
    elif userInput[0] == 'list':
        for i in catalogue.values():
            print('- ',i)
        pass
    elif userInput[0].lower() == 'see':
        if userInput[1].lower() in catalogue:
            catalogue[userInput[1]].see
    elif userInput[0] == '?':
        print('''
buyer \'name'\. to add buyer
seller \'name\'. to add seller
\'user name\' \'basket name\' add \'item name\'. to add item to basket (for buyer only)
\'user name\' new \'catalogue name\' \'item name\' \'count\'. to add new cataogue or new item (seller only)
\'user name\' basket list. to see baket list and item inside(buyer only)
list. to see catalogue list
see \'catalogue name\'. to see catalogue item list
exit. to end this progam
        ''')
    elif userInput[0].lower() =='exit':
        exit()
    else:
        if userInput[0].lower() in buyer:
            if userInput[2].lower() == 'add':
                if userInput[1] in userInput[0].basket:
                    userInput[1].add(userInput[3])
                else:
                    print('Unknow catalogue')
            pass
        if userInput[0].lower() in seller:
            pass
    
        


