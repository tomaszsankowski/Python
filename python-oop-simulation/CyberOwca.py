from Zwierze import Zwierze
import random

class CyberOwca(Zwierze):
    
    def __init__(self, x, y, swiat, sila=11, inicjatywa=4,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=11, inicjatywa=4,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "cyberowca.jpg"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = CyberOwca(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "CyberOwca"
    
    
    def akcja(self):
        self.ustawPoprzednie()
        self.wiek += 1

        barszcz = self.swiat.znajdzNajblizszyBarszcz(self.x, self.y)

        if barszcz is not None: # jesli na planszy jest jakikolwiek barszcz sosnowskiego to idzie w jego strone
            if barszcz.getX() < self.x:
                self.x -= 1
            elif barszcz.getX() > self.x:
                self.x += 1
            elif barszcz.getY() < self.y:
                self.y -= 1
            elif barszcz.getY() > self.y:
                self.y += 1
        else:  # jesli nie ma to idzie w przypadkowym kierunku
            randomise = random.randint(0, 3)
            if randomise == 0 and self.x > 0:
                self.x -= 1
            elif randomise == 1 and self.x < self.swiat.getM() - 1:
                self.x += 1
            elif randomise == 2 and self.y < self.swiat.getN() - 1:
                self.y += 1
            elif randomise == 3 and self.y > 0:
                self.y -= 1