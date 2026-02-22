from abc import ABC, abstractmethod

class Organizm(ABC):
    
    def __init__(self, x, y, swiat, sila=None, inicjatywa=None,  poprzednieX=None, poprzednieY=None, wiek=None):
        self.sila = sila if sila is not None else 0
        self.inicjatywa = inicjatywa if inicjatywa is not None else 0
        self.x = x
        self.y = y
        self.poprzednieX = poprzednieX if poprzednieX is not None else x
        self.poprzednieY = poprzednieY if poprzednieY is not None else y
        self.wiek = wiek if wiek is not None else 0
        self.swiat = swiat


    def getWiek(self):
        return self.wiek
    def setWiek(self, value):
        self.wiek = value


    def getInicjatywa(self):
        return self.inicjatywa
    def setInicjatywa(self, value):
        self.inicjatywa = value


    def getSila(self):
        return self.sila
    def setSila(self, value):
        self.sila = value


    def getX(self):
        return self.x
    def setX(self, value):
        self.x = value


    def getY(self):
        return self.y
    def setY(self, value):
        self.y = value
        
        
    @abstractmethod
    def getImie(self):
        pass

    @abstractmethod
    def akcja(self):
        pass

    @abstractmethod
    def kolizja(self, atakujacy):
        pass

    @abstractmethod
    def rysowanie(self):
        pass

    @abstractmethod
    def rozmnozSie(self, x, y, swiat):
        pass


    def czyOdbilAtak(self, atakujacy):
        return False

    def ustawPoprzednie(self):
        self.poprzednieX = self.x
        self.poprzednieY = self.y

    def cofnijRuch(self):
        self.x = self.poprzednieX
        self.y = self.poprzednieY

    def isHere(self, x, y):
        return self.x == x and self.y == y

    def organizmToString(self):
        return f"{self.getImie()} {self.sila} {self.inicjatywa} {self.x} {self.y} {self.poprzednieX} {self.poprzednieY} {self.wiek}"