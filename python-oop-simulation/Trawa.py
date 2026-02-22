from Roslina import Roslina

class Trawa(Roslina):
    
    def __init__(self, x, y, swiat, sila=0, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=0, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "Trawa.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Trawa(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Trawa"