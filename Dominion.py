from abc import ABCMeta, abstractmethod


class Card(metaclass=ABCMeta):
    '''
    This Abstract Class is used to only creat certain cards with at least the following
    '''

    @abstractmethod
    def name(self):         #for later accessing the name of each card
        pass
    @abstractmethod
    def playable(self):         # to determine wether it is a card that can actually be played or not
        pass
    @abstractmethod
    def price(self):            # for accessing the price of a card
        pass
    @abstractmethod
    def action(self):           # to access if the Card has an influence on the action a pla can do i his turn
        pass
    @abstractmethod
    def buy(self):              # to access if the Card has an influence on the buys a player can do in his turn
        pass
    @abstractmethod
    def effect(self):           # a special effect if the Card has one
        pass
    @abstractmethod
    def v_points(self):         # if it's a normal Card but gives Victory Points
        pass
    @abstractmethod
    def duration(self):         # if its a card that last longer than one turn on the field
        pass
class Monetary_Card(Card) :
    '''
    A Class only created for Cards used as Money in the game.
    '''
    def __init__(self,name,price,action,buy,effect,v_points,duration):
        self.name = name
        self.price = price
        self.action = action
        self.buy = buy
        self.effect = effect
        self.v_points = v_points
        self.duration = duration
        self.id = None          # this id will later be used for an easier Database referencing

    def name(self):
        return self.name
    def playable(self):
        return False
    def price(self):
        return self.price
    def action(self):
        return None
    def effect(self):
        return None
    def v_points(self):
        return self.v_points
    def duration(self):
        if self.duration != "" :
            return self.duration
        else :
            return 0
    def buy(self):
        return self.buy
    def gen_id(self):
       '''
       This method will be invoked right after generating a card--> intendet to register each card by hand in the Programm;
       not by codeing it in to the database
       '''
        pass
class Point_card(Card) :

    '''
    A Class only used to creat cards that mainly provied Victory points
    '''
    def __init__(self,name,price,action,buy,effect,v_points,duration):
        self.name = name
        self.price = price
        self.action = action
        self.buy = buy
        self.effect = effect
        self.v_points = v_points
        self.duration = duration
    def name(self):
        return self.name
    def playable(self):
        return False
    def price(self):
        return self.price
    def action(self):
        return None
    def effect(self):
        return None
    def v_points(self):
        return self.v_points
    def duration(self):
            return self.duration
    def gen_id(self):
       '''
       This method will be invoked right after generating a card--> intendet to register each card by hand in the Programm;
       not by codeing it in to the database
       '''
        pass
class Norm_Card (Card):
    '''
    The usual Card Type most of the cards will be
    '''
    def __init__(self,name,price,action,buy,effect,v_points,duration):
        self.name = name
        self.price = price
        self.action = action
        self.buy = buy
        self.effect = effect
        self.v_points = v_points
        self.duration = duration
    def name(self):
        return self.name
    def playable(self):
        return False
    def price(self):
        return self.price
    def action(self):
        return None
    def effect(self):
        return None
    def v_points(self):
        return self.v_points
    def duration(self):
            return self.duration
    def gen_id(self):
       '''
       This method will be invoked right after generating a card--> intendet to register each card by hand in the Programm;
       not by codeing it in to the database
       '''
        pass
class Deck :
    def __init__(self,name,editions):
        self.name = name
        self.editions = editions        # The plan is to get an input which is mapped into a list.
        self.m_cards=[]
        self.v_cards=[]
        self.n_cards=[]
        self.id = None
    def build(self,m_input,v_input,n_input):
        while (m_input and v_input and n_input) != "Q" :        #further work to be done for "endless" appendation to the classes cards lists

            self.m_cards.append(m_input)
            self.v_cards.append(v_input)
            self.n_cards.append(n_input)

    def gen_id(self):
        '''
        This method will be invoked right after generating a card--> intendet to register each Deck by hand in the Programm;
        not by codeing it in to the database
        '''
        pass

def new_cardtype(x,y,z):
    ''' A function to creat a new subclass of Card for future releases '''
    pass

def display():
    '''
    should provide a Global sight of the later GUI to display all Panels with its infos . Ex.: display selected Card type,
    all cards which have not been added of this type ,the availabel editions of the game , The current or other decks, all selected cards.
    '''
    pass
def acces_card():
    '''
    A method to get the needed data of the selected card, convert it and acces the Card_DB, read the other data from it to send it to display()
     or other functions that need the data.
    '''
    pass


s=Deck("New One","Basics")








s.build(mcard,vcard,ncard)
print(s.m_cards)
print(s.v_cards)
print(s.n_cards)
