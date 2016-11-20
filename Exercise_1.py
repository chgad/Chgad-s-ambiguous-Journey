import sequence
import Git_class
def max(a,b):
    if a>b :
        return a
    elif b>a :
        return b

def maax(args):
    print(len(args))
    print(len(args)-1)
    for a in range(len(args)-1,0,-1) :
        for i in range(a) :
            if args[i] < args[i+1]:
                temp =args[i]
                args[i]= args[i+1]
                args[i+1] = temp

    return args


class Mytupel(tuple):
    def __init__(self,tuple):
        self.t = tuple
        if len(self.t)>2:
            self.t=()
            #raise Initiation error                 comming soon, to make sure the tuple is just consisting of 2 variables
    def __lt__(self, other):
        if self.t[1]< other.t[1]:
            return -1

    def __gt__(self, other):
        if self.t[1] > other.t[1]:
            return 1
    def __eq__(self, other):
        if self.t[1]== other.t[1]:
            return 0


def maaax(adict):
    '''  A small yet use full function which takes a dictonary as variable.
    This dictionary get's "destructed" in to Key,Value Tuples which in the next line get mapped into Mytuples.
    The second mapping makes it possible for the bubble sort to evaluate by second argument , the cost of a card.
    The return value is the now a sorted list (high --> low) with Mytuple tuples as items.'''
    adict = adict.items()
    adict = [ Mytupel(k) for k in adict ]
    for a in range(len(adict)-1,0,-1):
        for i in range(a):
            if adict[i] < adict[i+1]:
                temp = adict[i]
                adict[i] = adict[i+1]
                adict[i+1] = temp
    return adict



dict = {"a": 1, "b": 2, "s": 15, "k": 1, "t": 55, "w": 9}

                            # compare by second variable in tuple

print(maaax(dict))

print(maax([1,2,4,2,6,9
            ]))

a = Mytupel(("a",3))
b = Mytupel(("b",7))
c = Mytupel(("c",1))
alist = [a, b, c]
#print(maaax(alist))
#print(alist)
