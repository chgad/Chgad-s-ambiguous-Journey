'''
Created on 04.10.2016

@author: Christian
'''

class Enum :
    """ Project for understanding certain functions and classes"""
    def __init__(self, int):
        self.n = int
        pass
    def rang(self):
        """ creates a list of int's from 0 up to n-1 --> n numbers like range()"""
        a = self.n - 1
        list = []
        while a>=0 :
            list.append(a)
            a -=1
        return list


class Account :
    '''
    Ein simpler Account
    '''
    accounts = 0

    def __init__(self, name, pw , date, region, mail):
        self.name = name
        self.date = date
        self.region = region
        self.pw = pw
        self.mail = mail
        Account.accounts += 1
        
    def storing_pw(self):
        store = open("PW_storage.txt", 'a')
        store.write(self.pw)
        store.close()
        print("Password stored!")
    def pw_request(self):
        c= 0
        while c < 3 :
            nam= input("waht is your name?")
            mai= input("waht is your mail address?")
            if (nam == self.name) and mai == self.mail :
                return print(self.pw)
        
            else :
                c +=1
                print("Access Denied! Try again. %i/3 Attempts" % c)
        

def numbers():
    natrual_number(10)
def natrual_number(n):
    a=0
    List=[]
    while n>0:
        a+=1
        List.append(a)
        n=n-1
        print(a)
#natrual_number(10)
numbers()
def grid():        # n ist zeile
    k = range(11)
    for a in k  :
        if a in [0,5,10]  :
            print("+ - - - - + - - - - +")
        else :
            print("|         |          |")


Sam = Account("Sam","123","01.01.00","europe","test@aox.com")
print(Sam.accounts)
Tina = Account("Tina","456","01.01.00","Asia","test2@aox.com")
print(Tina.accounts)
#Sam.storing_pw()
#Sam.pw_request()
#natrual_number(10)
#numbers()
#grid()

ran = Enum(10)
ran = ran.rang()
print (ran)
cliff = Enum(3)
cliff1=[method for method in dir(cliff) if callable(getattr(cliff, method))]
print(cliff1)

