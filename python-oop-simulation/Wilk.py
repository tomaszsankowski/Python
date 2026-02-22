from Zwierze import Zwierze

class Wilk(Zwierze):
    
    def __init__(self, x, y, swiat, sila=9, inicjatywa=5,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=9, inicjatywa=5,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "wilk.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Wilk(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Wilk"