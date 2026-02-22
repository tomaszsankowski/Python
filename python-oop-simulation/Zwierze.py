from Organizm import Organizm
import random

class Zwierze(Organizm):
    
    def __init__(self, x, y, swiat, sila=None, inicjatywa=None,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila, inicjatywa,  poprzednieX, poprzednieY, wiek)


    def rozmnazanie(self):  # zwierze podejmuje probe rozmnozenia w przypadkowym kierunku, jesli trafi na pole zajete - nie rozmnaza sie
        where = random.randint(0, 3)
        if where == 0 and self.x > 0 and self.swiat.isTaken(self.x - 1, self.y):
            self.rozmnozSie(self.x - 1, self.y, self.swiat)
            self.swiat.dodajLog(self.getImie() + " rozmnaza sie!")
            return
        elif where == 1 and self.x < self.swiat.getM() - 1 and self.swiat.isTaken(self.x + 1, self.y):
            self.rozmnozSie(self.x + 1, self.y, self.swiat)
            self.swiat.dodajLog(self.getImie() + " rozmnaza sie!")
            return
        elif where == 2 and self.y < self.swiat.getN() - 1 and self.swiat.isTaken(self.x, self.y + 1):
            self.rozmnozSie(self.x, self.y + 1, self.swiat)
            self.swiat.dodajLog(self.getImie() + " rozmnaza sie!")
            return
        elif where == 3 and self.y > 0 and self.swiat.isTaken(self.x, self.y - 1):
            self.rozmnozSie(self.x, self.y - 1, self.swiat)
            self.swiat.dodajLog(self.getImie() + " rozmnaza sie!")
            return
        self.swiat.dodajLog(self.getImie() + " probowal sie rozmnozyc, ale mu nie wyszlo!")
        return


    def kolizja(self, atakujacy):
        if self.czyOdbilAtak(atakujacy):  # odbijanie ataku
            self.swiat.dodajLog(self.getImie() + " odbil atak " + atakujacy.getImie())
            atakujacy.cofnijRuch()
            return
        elif type(self) == type(atakujacy):  # rozmnazanie
            if isinstance(atakujacy, Zwierze) and self.swiat.sprawdzCzyZyje(atakujacy) and isinstance(self, Zwierze) and self.swiat.sprawdzCzyZyje(self):
                atakujacy.cofnijRuch()
                self.rozmnazanie()
            return
        elif atakujacy.getSila() >= self.sila:  # atakujacy wygrywa
            self.swiat.dodajLog(atakujacy.getImie() + " zabil " + self.getImie())
            self.swiat.zabijOrganizm(self)
            return
        else:  # atakujacy przegrywa
            self.swiat.dodajLog(atakujacy.getImie() + " zginal probujac atakowac " + self.getImie())
            self.swiat.zabijOrganizm(atakujacy)
            return


    def akcja(self):  # zwierze udaje sie na przypadkowe pole
        self.ustawPoprzednie()
        self.wiek+=1
        randomise = random.randint(0,3)
        if randomise == 0 and self.x>0:
            self.x-=1
        elif randomise == 1 and self.x < self.swiat.getM() - 1:
            self.x+=1
        elif randomise == 2 and self.y < self.swiat.getN() - 1:
            self.y+=1
        elif randomise == 3 and self.y < 0:
            self.y-=1