import random
import sys
from typing import cast
from Organizm import Organizm
from Roslina import Roslina
from Zwierze import Zwierze
from Czlowiek import Czlowiek
from Antylopa import Antylopa
from Lis import Lis
from Owca import Owca
from Wilk import Wilk
from Zlow import Zlow
from BarszczSosnowskiego import BarszczSosnowskiego
from Guarana import Guarana
from WilczeJagody import WilczeJagody
from Trawa import Trawa
from Mlecz import Mlecz
from CyberOwca import CyberOwca
from tkinter import simpledialog, messagebox

class Swiat:
        
    def __init__(self, m, n):
        self.m = m
        self.n = n
        pola = m*n
        self.iloscOrganizmow = int(((pola - pola % 100) / 100) * 11 + 1)
        print("Swiat o wymiarach",self.m ,self.n)
        self.organizmy = []
        self.czyZyje = []
        self.czyZyje.append(True)
        self.organizmy.append(Czlowiek(m//2,n//2,self))
        self.tarczaAlzuraCzlowieka = -5
        
        for i in range(1,self.iloscOrganizmow):
            self.czyZyje.append(True)
            losx = random.randint(0,m-1)
            losy = random.randint(0,n-1)
            while not self.czyZajete(losx, losy, i):
                losx = random.randint(0, m - 1)
                losy = random.randint(0, n - 1)
            if i % 11 == 0:
                self.organizmy.append(Antylopa(losx, losy, self))
            elif i % 11 == 1:
                 self.organizmy.append(BarszczSosnowskiego(losx, losy, self))
            elif i % 11 == 2:
                 self.organizmy.append(Guarana(losx, losy, self))
            elif i % 11 == 3:
                self.organizmy.append(Lis(losx, losy, self))
            elif i % 11 == 4:
                self.organizmy.append(Mlecz(losx, losy, self))
            elif i % 11 == 5:
                self.organizmy.append(Owca(losx, losy, self))
            elif i % 11 == 6:
                self.organizmy.append(Trawa(losx, losy, self))
            elif i % 11 == 7:
                self.organizmy.append(WilczeJagody(losx, losy, self))
            elif i % 11 == 8:
                self.organizmy.append(Wilk(losx, losy, self))
            elif i % 11 == 9:
                self.organizmy.append(Zlow(losx, losy, self))
            elif i % 11 == 10:
                self.organizmy.append(CyberOwca(losx, losy, self))

        self.logi = []
        
        self.wczytanoSwiat = False
            
            
    def zakonczGre(self):
        sys.exit()


    def dodawanieOrganizmu(self, i, j, selected_value):
        if selected_value is not None:
            # Twój kod dodawania organizmu na podstawie wartości orgName
            if selected_value == "Antylopa":
                self.dodajOrganizm(Antylopa(i, j, self))
            elif selected_value == "BarszczSosnowskiego":
                self.dodajOrganizm(BarszczSosnowskiego(i, j, self))
            elif selected_value == "Guarana":
                self.dodajOrganizm(Guarana(i, j, self))
            elif selected_value == "Lis":
                self.dodajOrganizm(Lis(i, j, self))
            elif selected_value == "Mlecz":
                self.dodajOrganizm(Mlecz(i, j, self))
            elif selected_value == "Owca":
                self.dodajOrganizm(Owca(i, j, self))
            elif selected_value == "Trawa":
                self.dodajOrganizm(Trawa(i, j, self))
            elif selected_value == "WilczeJagody":
                self.dodajOrganizm(WilczeJagody(i, j, self))
            elif selected_value == "Wilk":
                self.dodajOrganizm(Wilk(i, j, self))
            elif selected_value == "Zlow":
                self.dodajOrganizm(Zlow(i, j, self))
            elif selected_value == "Czlowiek":
                self.dodajOrganizm(Czlowiek(i, j, self))
            elif selected_value == "CyberOwca":
                self.dodajOrganizm(CyberOwca(i, j, self))


    def wykonajTure(self, event):  # zwraca True jesli czlowiek zginal w czasie gry
        key = event.keysym

        if key in ['w', 'a', 's', 'd', 'z', 'l', 'q', 'p']:
            humanIndex = 0
            if key in ['z', 'l', 'q', 'p']:
                czyRuch = False
            else:
                czyRuch = True
            self.sortujOrganizmy()
            iterations = self.iloscOrganizmow
            for i in range(iterations):
                if isinstance(self.organizmy[i], Czlowiek):  # tura człowieka
                    czl = cast(Czlowiek, self.organizmy[i])
                    if self.wczytanoSwiat:
                        self.wczytanoSwiat = False
                    self.tarczaAlzuraCzlowieka = czl.getTarczaAlzura()

                    humanIndex = i
                    if not self.czyZyje[i]:
                        return True
                    else:
                        if(czyRuch):
                            self.organizmy[i].akcja()

                        if key in ['w', 'a', 's', 'd']:
                            if czl.ruchCzlowieka(key, self.m, self.n):
                                for k in range(iterations):
                                    if self.czyZyje[k] and (k != i) and (self.organizmy[i].getX() == self.organizmy[k].getX()) and (self.organizmy[i].getY() == self.organizmy[k].getY()):
                                        self.organizmy[k].kolizja(self.organizmy[i])
                        elif key == 'z':
                            self.zapiszSwiat()
                        elif key == 'q':
                            return True
                        elif key == 'l':
                            self.wczytajSwiat()
                            self.wczytanoSwiat = True
                            break
                        elif key == 'p':
                            if czl.getTarczaAlzura() == -5:
                                czl.setTarczaAlzura(4)
                            else:
                                self.dodajLog("Nie można aktywować supermocy!")
                else:  # tura innego organizmu
                    if not self.wczytanoSwiat and czyRuch:
                        if self.czyZyje[i]:
                            self.organizmy[i].akcja()
                            for k in range(iterations):
                                if self.czyZyje[k] and (k != i) and (self.organizmy[i].getX() == self.organizmy[k].getX()) and (self.organizmy[i].getY() == self.organizmy[k].getY()):
                                    self.organizmy[k].kolizja(self.organizmy[i])
                                    
            if(not self.czyZyje[humanIndex]):
                return True
            return False


    def sortujOrganizmy(self):
        for i in range(self.iloscOrganizmow - 1):
            for j in range(self.iloscOrganizmow - i - 1):
                if self.organizmy[j].getInicjatywa() < self.organizmy[j + 1].getInicjatywa():
                    self.organizmy[j], self.organizmy[j + 1] = self.organizmy[j + 1], self.organizmy[j]
                    self.czyZyje[j], self.czyZyje[j + 1] = self.czyZyje[j + 1], self.czyZyje[j]
                elif self.organizmy[j].getInicjatywa() == self.organizmy[j + 1].getInicjatywa():
                    if self.organizmy[j].getWiek() < self.organizmy[j + 1].getWiek():
                        self.organizmy[j], self.organizmy[j + 1] = self.organizmy[j + 1], self.organizmy[j]
                        self.czyZyje[j], self.czyZyje[j + 1] = self.czyZyje[j + 1], self.czyZyje[j]


    def czyZajete(self, x, y, iterator): # zwraca True jesli pole jest wolne
        for i in range(iterator):
            if self.organizmy[i] is None:
                continue
            if self.organizmy[i].isHere(x, y) and self.czyZyje[i]:
                return False
        return True


    def isTaken(self, x, y): # zwraca True jesli pole jest wolne
        for i in range(self.iloscOrganizmow):
            if self.organizmy[i] is None:
                continue
            if self.organizmy[i].isHere(x, y) and self.czyZyje[i]:
                return False
        return True
    
    
    def getOkupant(self, x, y):  # zwaca organizm jesli sie znajduje na danym polu lub None jesli pole jest niezajete
        for i in range(self.iloscOrganizmow):
            if self.organizmy[i] is None:
                continue
            if self.czyZyje[i] and self.organizmy[i].isHere(x, y):
                return self.organizmy[i]
        return None


    def zabijOrganizm(self, x=None, y=None):
        if y is None:
            biedak = x
            for i in range(self.iloscOrganizmow):
                if self.organizmy[i].isHere(biedak.getX(), biedak.getY()) and self.organizmy[i].getImie() == biedak.getImie():
                    self.czyZyje[i] = False
                    break
        else:
            for i in range(self.iloscOrganizmow):
                if self.organizmy[i].isHere(x, y):
                    self.czyZyje[i] = False


    def sprawdzCzyZyje(self, x=None, y=None):
        if y is None:
            org = x
            for i in range(self.iloscOrganizmow):
                if self.organizmy[i] == org:
                    return self.czyZyje[i]
        else:
            for i in range(self.iloscOrganizmow):
                if self.czyZyje[i] and self.organizmy[i].isHere(x, y):
                    return True


    def zabijZwierze(self, x, y):
        for i in range(self.iloscOrganizmow):
            if isinstance(self.organizmy[i], Zwierze) and self.czyZyje[i] and not isinstance(self.organizmy[i], CyberOwca):
                if self.organizmy[i].isHere(x, y):
                    self.czyZyje[i] = False
                    self.logi.append(self.organizmy[i].getImie() + " za bardzo zblizyl sie do barszczu sosnowskiego")


    def dodajOrganizm(self, organizm):
        if self.isTaken(organizm.getX(), organizm.getY()):
            nowa_tablica = self.organizmy + [organizm]
            nowe_czy_zyje = self.czyZyje + [True]
            self.iloscOrganizmow += 1
            self.organizmy = nowa_tablica
            self.czyZyje = nowe_czy_zyje
        else:
            organizm = None


    def wczytajSwiat(self):  # wczytywanie zapisu gry
        nazwa = simpledialog.askstring("Wczytaj stan gry", "Wpisz nazwę pliku, z którego chcesz wczytać stan gry:")
        nazwa += ".txt"
        try:
            with open(nazwa, "r") as plik:
                m, n, iloscOrganizmow, tarczaAlzura = map(int, plik.readline().split())

                self.organizmy.clear()
                self.czyZyje.clear()

                for _ in range(iloscOrganizmow):
                    linia = plik.readline().split()
                    zycie = int(linia[0])
                    orgNamex = linia[1]
                    sila, inicjatywa, x, y, poprzednieX, poprzednieY, wiek = map(int, linia[2:])

                    if(zycie == 1):
                        self.czyZyje.append(True)
                    else:
                        self.czyZyje.append(False)
                    orgName = orgNamex

                    if orgName == "Antylopa":
                        self.organizmy.append(Antylopa(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "BarszczSosnowskiego":
                        self.organizmy.append(BarszczSosnowskiego(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Guarana":
                        self.organizmy.append(Guarana(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Lis":
                        self.organizmy.append(Lis(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Mlecz":
                        self.organizmy.append(Mlecz(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Owca":
                        self.organizmy.append(Owca(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Trawa":
                        self.organizmy.append(Trawa(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "WilczeJagody":
                        self.organizmy.append(WilczeJagody(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Wilk":
                        self.organizmy.append(Wilk(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Zlow":
                        self.organizmy.append(Zlow(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))
                    elif orgName == "Czlowiek":
                        self.organizmy.append(Czlowiek(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek, tarczaAlzura))
                    elif orgName == "CyberOwca":
                        self.organizmy.append(CyberOwca(x, y, self, sila, inicjatywa,  poprzednieX, poprzednieY, wiek))

                self.m = m
                self.n = n
                self.iloscOrganizmow = iloscOrganizmow
                messagebox.showinfo("Wczytano stan gry", "Wczytano stan gry pomyślnie!")
        except FileNotFoundError:
            sys.exit()


    def zapiszSwiat(self):  # zapisanie stanu gry
        nazwa = simpledialog.askstring("Zapisz stan gry", "Wpisz nazwę pliku, do którego chcesz zapisać stan gry:")
        nazwa += ".txt"
        try:
            with open(nazwa, "w") as plik:
                plik.write(f"{self.m} {self.n} {self.iloscOrganizmow} {self.tarczaAlzuraCzlowieka}\n")
                for i in range(self.iloscOrganizmow):
                    if(self.czyZyje[i]):
                        zycie = 1
                    else:
                        zycie = 0
                    plik.write(f"{zycie} {self.organizmy[i].organizmToString()}\n")
                messagebox.showinfo("Zapisano stan gry", "Zapisano stan gry pomyślnie!")
        except FileNotFoundError:
            sys.exit()


    def znajdzNajblizszyBarszcz(self, x, y):  # zwraca barszcz sosnowskiego najblizej cyber owcy lub None jezeli nie ma zadnego na mapie
        barszcz = None
        minDroga = float('inf')
        
        for i in range (self.iloscOrganizmow):
            organizm = self.organizmy[i]
            if isinstance(organizm, BarszczSosnowskiego) and self.czyZyje[i]:
                droga = abs(organizm.x - x) + abs(organizm.y - y)
                if(minDroga > droga):
                    minDroga = droga
                    barszcz = organizm
               
        return barszcz
    
    
    def dodajLog(self, log):
        self.logi.append(log)


    def getM(self):
        return self.m
    
    
    def getN(self):
        return self.n