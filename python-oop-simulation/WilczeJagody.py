from Roslina import Roslina


class WilczeJagody(Roslina):
    
    def __init__(self, x, y, swiat, sila=99, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=99, inicjatywa=0,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "jagody.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = WilczeJagody(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)
        return


    def getImie(self):
        return "WilczeJagody"
    
    
    def kolizja(self,atakujacy):  # kazdy organizm probojacy zjesc wilcze jagody ginie
        self.swiat.dodajLog( atakujacy.getImie() + " zginal probujac zjesc " + self.getImie())
        self.swiat.zabijOrganizm(atakujacy)
        return