from Zwierze import Zwierze
import random

class Owca(Zwierze):
    
    def __init__(self, x, y, swiat, sila=4, inicjatywa=4,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=4, inicjatywa=4,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "owca.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Owca(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Owca"