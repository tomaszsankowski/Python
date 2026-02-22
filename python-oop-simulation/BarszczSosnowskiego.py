from Roslina import Roslina
import random
from CyberOwca import CyberOwca

class BarszczSosnowskiego(Roslina):
    
    def __init__(self, x, y, swiat, sila=10, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=10, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "barszcz.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = BarszczSosnowskiego(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)
       
        
    def kolizja(self, atakujacy):  # kazde zwierze oprocz cyber owcy jak sprobuje zjesc barszcz, ginie
        if isinstance(atakujacy, CyberOwca):
            self.swiat.dodajLog(atakujacy.getImie() + " zjadla " + self.getImie())
            self.swiat.zabijOrganizm(self)
            return
        else:
            self.swiat.dodajLog(atakujacy.getImie() + " zginal probujac zjesc" + self.getImie())
            self.swiat.zabijOrganizm(atakujacy)
            return


    def getImie(self):
        return "BarszczSosnowskiego"
    
    
    def akcja(self):
        self.ustawPoprzednie()
        self.wiek += 1
        self.swiat.zabijZwierze(self.x, self.y - 1)  # zabija wszystkie zwierzęta dookoła
        self.swiat.zabijZwierze(self.x, self.y + 1)
        self.swiat.zabijZwierze(self.x + 1, self.y)
        self.swiat.zabijZwierze(self.x - 1, self.y)
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