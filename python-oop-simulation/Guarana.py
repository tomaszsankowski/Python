from Roslina import Roslina

class Guarana(Roslina):
    
    def __init__(self, x, y, swiat, sila=0, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=0, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "guarana.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Guarana(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Guarana"
    
    
    def kolizja(self, atakujacy):
        atakujacy.setSila(atakujacy.getSila() + 3)
        self.swiat.zabijOrganizm(self)
        self.swiat.dodajLog(atakujacy.getImie() + " zjadl " + self.getImie())
        return