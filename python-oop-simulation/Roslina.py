import random
from Organizm import Organizm

class Roslina(Organizm):
    
    def __init__(self, x, y, swiat, sila=None, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila, inicjatywa,  poprzednieX, poprzednieY, wiek)


    def akcja(self):
        self.ustawPoprzednie()
        self.wiek += 1
        randomise = random.randint(0, 9)
        if randomise == 0:  # 10% szans na próbę rozmnożenia
            where = random.randint(0, 3)
            if where == 0 and self.x > 0:
                self.rozmnozSie(self.x - 1, self.y, self.swiat)
            elif where == 1 and self.x < self.swiat.getM() - 1:
                self.rozmnozSie(self.x + 1, self.y, self.swiat)
            elif where == 2 and self.y < self.swiat.getN() - 1:
                self.rozmnozSie(self.x, self.y + 1, self.swiat)
            elif where == 3 and self.y > 0:
                self.rozmnozSie(self.x, self.y - 1, self.swiat)


    def kolizja(self, atakujacy):  # domyslnie, roslina zawsze przegrywa walke
        self.swiat.zabijOrganizm(self)
        self.swiat.dodajLog(atakujacy.getImie() + " zjadł " + self.getImie())
        return
