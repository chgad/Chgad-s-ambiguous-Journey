'''
Created on 04.10.2016

@author: Christian
'''
import tkinter
import swampy.TurtleWorld

class Enum :
    """ Project for understanding certain functions and classes"""
    def __init__(self, int):
        self.n = int
        pass
    
    def natrual_number(self):
        a=0
        List=[]
        while self.n >0:
            a+=1
            List.append(a)
            self.n-=1
        return List
    
    def rang(self):
        """ creates a list of int's from 0 up to n-1 --> n numbers like range()"""
        #print(natrual_number())
        
        
        '''a = self.n - 1
        list = []
        while a>=0 :
            list.append(a)
            a -=1
        return list'''
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
        


def grid(z,s,h,w):                  # n ist zeile,s spalte, h hight,w width
    if (type(z),type(s),type(h),type(w)) == (int,int,int,int):
        if z>0 and s>0 and h>0 and w>0:
            head_a = "+" + " - "*w          #Trenner design (horizontal)
            ele_a  = "|" + "   "*w          #Trenner design (vertikal)
            while z>0 :                     # loop über Zeilen
                print(head_a*s , "+")
                for i in range(h):          # loop über höhe der Kästen
                    print(ele_a*s + ' |' )
                z -= 1
            if z == 0 :                     # Abschluss des Rasters
                print(head_a*s , "+")
        else :
            print("Please only enter positive integers!")
    else :
        print("Please enter integers only!")
        
#Sam = Account("Sam","123","01.01.00","europe","test@aox.com")
#print(Sam.accounts)
#Tina = Account("Tina","456","01.01.00","Asia","test2@aox.com")
#print(Tina.accounts)
#Sam.storing_pw()
#Sam.pw_request()
#natrual_number(10)
#numbers()
#grid()

ran = Enum(10)
ran = ran.natrual_number()
print (ran)
#cliff = Enum(3)
#cliff1=[method for method in dir(cliff) if callable(getattr(cliff, method))]
#print(cliff1)
grid(4,4,4,4)

