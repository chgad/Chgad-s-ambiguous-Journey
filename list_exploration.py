import re
import string


f = open("lists.txt","a")
test_list = ["a","b","c","d"]
#for d in test_list:
#    f.write(d+" ")
f.close()

f = open("lists.txt","r")

text = f.read()
f.close()
pattern = re.compile(r"(a b c)")
groups = pattern.findall(text)
x=0



for f in groups:
    x += 1

print("'a b c'exists %i times" % x)

def read_file(filename):
    ''' A simple reading function. Needs the name of the file to be read as parameter.
    returns the given text as string.
    :param: filename
    :return: text as string
    '''
    f = open(filename, "r")
    text = f.read()
    f.close()
    return text

def pars_File(filename):
    ''' This function parses a file. It takes one parameter , the files name , converts it to a string, gets it tp be
    read an then does it's magic. The return is a List of (str, int) Tuples where the str's are the words; sorted by
    Alphabet and cases, an the int's the number of occurences in the file.
    :param: filename
    :return:
    '''

    rank={}
    filename = str(filename)
    text = read_file(filename)
    exclude = set(string.punctuation)
    text = "".join(k for k in text if k not in exclude)
    strips = text.split(" ")
    for a in strips :
        if a not in rank:
            num=strips.count(a)
            rank[a] = num
    plan = sorted(rank, key=str.lower)
    for a in plan:
        print("The word %s apears %i times in the File." % (a,rank[a]) )

def take_order():
    ''' A simple function for taking orders
    '''
    order = input("What do you liek to order ? (Q) to quit. :").capitalize()
    ordered = []
    while order is not "Q" :
         ordered.append(order)
         order = input("Anything else ? (Q) to quit.").capitalize()
         print("Again.")
    else :
            print("Thanks for your Orders. You ordered:",ordered)

class Four_wins:
    def __init__(self,):
        self.field = [["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""]
                  ]
    def check():
        pass
    def show_field(self):
        for i in self.field :
            print(i)

    def player_1(column):
        pointer= "x"

    def player_2(self,column):
        pointer = "o"
        for i in range(5,-1,-1):
            if self.field[i][column] is not "":
                pass
            else:
                self.field[i][column] = pointer#
                break
        return self.show_field()

win= Four_wins()
print(type(win))
win.player_2(2)
for i in range(4):
    print("")
win.player_2(2)
#pars_File("lists.txt")
#take_order()

t=0

