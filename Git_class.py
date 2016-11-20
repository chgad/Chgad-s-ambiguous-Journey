'''
Created on 04.10.2016

@author: Christian
'''
from math import *
class Vector :
    def __init__(self,x,y,z) :
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        sum_z = self.z + other.z
        return Vector(sum_x,sum_y,sum_z)
    def distance(self):
        dis = sqrt(self.x**2 + self.y**2 + self.z**2)
        return dis
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
class n_Dim_Vector(Vector):

    def __init__(self,*args):
        # i 'd like to creat a class, which can handle any n- dimensional vector
        '''First idea : self.components= args
                    for i in sef.components and k in range(len(self.components)) :
                        x_k = i
        in this case i is the real value of each komponent and k just declars which komponent it is (x_0, x_1 ,...)'''
        self.components= args
        self.k = 0
        for i in self.components:           #counts the dimension of the vector
            self.k +=1
        self.x_h= (i for i in self.components)

    def print_Vector(self):                #tests to be done
        for k in range(len(self.magni)) :
            print("x_%i =" % k , self.x_k)
            
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
        


def grid(z,s,h,w):                          # n ist zeile,s spalte, h hight,w width
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
        
Sam = Account("Sam","123","01.01.00","europe","test@aox.com")
#print(Sam.accounts)
#Tina = Account("Tina","456","01.01.00","Asia","test2@aox.com")
#print(Tina.accounts)
#Sam.storing_pw()
#Sam.pw_request()
#natrual_number(10)
#numbers()
#grid()


'''CLASS : Enum test'''
ran = Enum(2)
ran = ran.natrual_number()
print (ran)

grid(4,4,4,4)
'''CLASS : Vector test'''
#a = Vector(1, 1, 2)
#b = Vector(-1,-1,-2)
#print(a.distance())
v = n_Dim_Vector(1,2)
print(v.components)
print(v.x_h)
print("Test")


# Riemann reihe

def rieman(n):
    sum = 0
    for n in range(n):
        k=(-1)** n*(1/(n+1))
        print(k)
        sum += k
    return sum
