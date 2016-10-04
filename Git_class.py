'''
Created on 04.10.2016

@author: Christian
'''

class Account :
    '''
    Ein simpler Account
    '''
    accounts = 0

    def __init__(self, name, pw , date, region):
        self.name = name
        self.date = date
        self.region = region
        Account.accounts += 1
        

Sam = Account("Sam","123","01.01.00","europe")
print(Sam.accounts)
Tina = Account("Tina","456","01.01.00","Asia")
print(Tina.accounts)