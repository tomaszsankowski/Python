from Zwierze import Zwierze
import random

class Lis(Zwierze):
    
    def __init__(self, x, y, swiat, sila=3, inicjatywa=7,  poprzednieX=None, poprzednieY=None, wiek=None):
        super().__init__(x, y, swiat, sila=3, inicjatywa=7,  poprzednieX=None, poprzednieY=None, wiek=None)


    def rysowanie(self):
        return "lis.png"


    def rozmnozSie(self, x, y, swiat):
        nowyOrganizm = Lis(x, y, swiat)
        swiat.dodajOrganizm(nowyOrganizm)


    def getImie(self):
        return "Lis"


    def akcja(self):  # idzie na przypadkowe pole, jesli po 10 probach bedzie trafial na same zajete to pozostaje w miejscu
        self.ustawPoprzednie()
        self.wiek += 1
        counter = 0
        while True:
            randomise = random.randint(0, 3)
            if randomise == 0 and self.x > 0:
                if not self.swiat.isTaken(self.x - 1, self.y):
                    okupant = self.swiat.getOkupant(self.x - 1, self.y)
                    if okupant.getSila() <= self.sila:
                        self.x -= 1
                        return
                else:
                    self.x-=1
                    return
            elif randomise == 1 and self.x < self.swiat.getM() - 1:
                if not self.swiat.isTaken(self.x + 1, self.y):
                    okupant = self.swiat.getOkupant(self.x + 1, self.y)
                    if okupant.getSila() <= self.sila:
                        self.x += 1
                        return
                else:
                    self.x+=1
                    return
            elif randomise == 2 and self.y < self.swiat.getN() - 1:
                if not self.swiat.isTaken(self.x, self.y + 1):
                    okupant = self.swiat.getOkupant(self.x, self.y + 1)
                    if okupant.getSila() <= self.sila:
                        self.y += 1
                        return
                else:
                    self.y+=1
                    return
            elif randomise == 3 and self.y > 0:
                if not self.swiat.isTaken(self.x, self.y - 1):
                    okupant = self.swiat.getOkupant(self.x, self.y - 1)
                    if okupant.getSila() <= self.sila:
                        self.y -= 1
                        return
                else:
                    self.y-=1
                    return
            counter+=1
            if counter > 10:
                return

