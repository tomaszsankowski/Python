from Roslina import Roslina
import random

class Mlecz(Roslina):
    
    def __init__(self, x, y, swiat, sila=0, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=0, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "mlecz.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Mlecz(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Mlecz"


    def akcja(self):
        self.ustawPoprzednie()
        self.wiek+=1
        for i in range (0,3): #3 proby rozmnozenia
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