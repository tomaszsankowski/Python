from Zwierze import Zwierze
from random import randint, choice
import random

class Antylopa(Zwierze):
    
    def __init__(self, x, y, swiat, sila=4, inicjatywa=4,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=4, inicjatywa=4,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "antylopa.png"


    def kolizja(self, atakujacy):
        willEscape = choice([False, True]) # dla True antylopa ucieka, dla False walczy
        if willEscape:
            directions = [(self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y + 1), (self.x, self.y - 1)]
            x, y = choice(directions)
            if self.swiat.isTaken(x, y):
                willEscape = False
            else:
                self.x = x
                self.y = y
                self.swiat.dodajLog("Antylopa uciekla przed atakiem!")
                return
        if not willEscape:
            if self.czyOdbilAtak(atakujacy): # odbijanie ataku
                self.swiat.dodajLog(self.getImie() + " odbil atak " + atakujacy.getImie())
                atakujacy.cofnijRuch()
                return
            elif self.getImie() == atakujacy.getImie(): # rozmnazanie
                if isinstance(atakujacy, Zwierze) and self.swiat.sprawdzCzyZyje(atakujacy) and isinstance(self, Zwierze) and self.swiat.sprawdzCzyZyje(self):
                    atakujacy.cofnijRuch()
                    self.rozmnazanie()
                return
            elif atakujacy.getSila() >= self.sila: # atakujacy wygrywa
                self.swiat.zabijOrganizm(self)
                self.swiat.dodajLog(atakujacy.getImie() + " zabil " + self.getImie())
                return
            else: # atakujacy przegrywa
                self.swiat.dodajLog(atakujacy.getImie() + " zginal probujac atakowac " + self.getImie())
                self.swiat.zabijOrganizm(atakujacy)
                return


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Antylopa(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Antylopa"


    def akcja(self):  # antylopa moze przeskoczyc o 2 pola
        self.ustawPoprzednie()
        randomise = random.randint(0, 7)
        if randomise == 0 and self.x > 0:
            self.x -= 1
        elif randomise == 1 and self.x < self.swiat.getM() - 1:
            self.x += 1
        elif randomise == 2 and self.y < self.swiat.getN() - 1:
            self.y += 1
        elif randomise == 3 and self.y > 0:
            self.y -= 1
        elif randomise == 4 and self.x < self.swiat.getM() - 2:
            self.x += 2
        elif randomise == 5 and self.y < self.swiat.getN() - 2:
            self.y += 2
        elif randomise == 6 and self.y > 1:
            self.y -= 2
        elif randomise == 7 and self.x > 1:
            self.x -= 2
        self.wiek += 1

