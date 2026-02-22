from Zwierze import Zwierze
import random

class Zlow(Zwierze):
    
    def __init__(self, x, y, swiat, sila=2, inicjatywa=1,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=2, inicjatywa=1,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "zlow.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Zlow(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Zlow"
    
    
    def czyOdbilAtak(self, atakujacy):
        if atakujacy.getSila() < 5:
            return True
        else:
            return False

        
    def akcja(self):  # zlow ma 25% szans na zmiane swojego aktualnego polozenia
        self.ustawPoprzednie()
        self.wiek += 1
        moveIf0 = random.randint(0, 3)
        randomise = random.randint(0, 3)
        if moveIf0 % 4 == 0:
            if randomise == 0 and self.x > 0:
                self.x -= 1
            elif randomise == 1 and self.x < self.swiat.getM() - 1:
                self.x += 1
            elif randomise == 2 and self.y < self.swiat.getN() - 1:
                self.y += 1
            elif randomise == 3 and self.y > 0:
                self.y -= 1