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
    def no_abstract(self):
        return "not abstract"

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

class Deck :
    def __init__(self,name,editions):
        self.name = name
        self.editions = editions        # The plan is to get an input which is mapped into a list.
        self.m_cards=[]
        self.v_cards=[]
        self.n_cards=[]

    def build(self,m_input,v_input,n_input):
        while (m_input and v_input and n_input) != "Q" :        #further work to be done for "endless" appendation to the classes cards lists

            self.m_cards.append(m_input)
            self.v_cards.append(v_input)
            self.n_cards.append(n_input)


s=Deck("New One","Basics")

mcard=input("Monetary Cards pls !")
vcard=input("Victory Point Cards pls!")
ncard=input("Normal Cards pls!")

s.build(mcard,vcard,ncard)
print(s.m_cards)
print(s.v_cards)
print(s.n_cards)
