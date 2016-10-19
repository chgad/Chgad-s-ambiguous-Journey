from abc import ABCMeta, abstractmethod


class Card(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        pass
    @abstractmethod
    def playable(self):
        pass
    @abstractmethod
    def price(self):
        pass
    @abstractmethod
    def action(self):
        pass
    @abstractmethod
    def buy(self):
        pass
    @abstractmethod
    def effect(self):
        pass
    @abstractmethod
    def v_points(self):
        pass
    @abstractmethod
    def duration(self):
        pass
class Monetary_Card(Card) :

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
        return self.buy_value
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



New_Card = Monetary_Card("Kupfer",0,0,0,"This is worth 1 Dime",0,0)

class new :
    def __init__(self):
        pass


