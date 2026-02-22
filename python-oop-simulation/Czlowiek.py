from Zwierze import Zwierze
from random import randint, choice
import random

class Czlowiek(Zwierze):
    
    def __init__(self, x, y, swiat, sila=5, inicjatywa=4, poprzednieX=None, poprzednieY=None, wiek=None, tarczaAlzura=-5):
        self.tarczaAlzura = tarczaAlzura
        super().__init__(x, y, swiat, sila, inicjatywa, poprzednieX, poprzednieY, wiek)


    def rysowanie(self):
        return "czlowiek.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Czlowiek(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Czlowiek"


    def getTarczaAlzura(self):
        return self.tarczaAlzura


    def setTarczaAlzura(self, t):
        self.tarczaAlzura = t


    def ruchCzlowieka(self, arrowKey, m, n):  # zwraca false jesli chcemy wyjsc poza plansze, wtedy ruch pomijamy
        self.ustawPoprzednie()
        if arrowKey == "a":  # LEFT
            if self.x > 0:
                self.setX(self.x - 1)
            else:
                return False
        elif arrowKey == "d":  # RIGHT
            if self.x < m - 1:
                self.setX(self.x + 1)
            else:
                return False
        elif arrowKey == "w":  # UP
            if self.y > 0:
                self.setY(self.y - 1)
            else:
                return False
        elif arrowKey == "s":  # DOWN
            if self.y < n - 1:
                self.setY(self.y + 1)
            else:
                return False
        else:
            return False
        return True


    def czyOdbilAtak(self, atakujacy):
        if self.tarczaAlzura >= 0:
            return True
        else:
            return False


    def akcja(self):
        self.wiek += 1
        if self.tarczaAlzura > -5:
            self.tarczaAlzura -= 1
        if self.tarczaAlzura >= 0:
            self.swiat.dodajLog(f"Zostało {self.tarczaAlzura+1} rund z tarczą Alzura!")
        elif self.tarczaAlzura == -5:
            self.swiat.dodajLog("Możesz aktywować tarczę Alzura!")
        else:
            self.swiat.dodajLog(f"Możesz aktywować tarczę Alzura za {self.tarczaAlzura+5} rund!")
