'''
Created on 04.10.2016

@author: Christian
'''

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
        
Sam = Account("Sam","123","01.01.00","europe","test@aox.com")
print(Sam.accounts)
Tina = Account("Tina","456","01.01.00","Asia","test2@aox.com")
print(Tina.accounts)
Sam.storing_pw()
Sam.pw_request()