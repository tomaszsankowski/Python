import tkinter as tk
import sys
from Swiat import Swiat
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox

class GUI:
    
    def __init__(self):
        def start_game():
            szerokosc = int(scale_szerokosc.get())
            wysokosc = int(scale_wysokosc.get())

            label_szerokosc.destroy()  # usuwamy cala zawartosc okienka oprocz nazwy gry i guzika 'zakoncz gre'
            scale_szerokosc.destroy()
            label_wysokosc.destroy()
            scale_wysokosc.destroy()
            button_start.destroy()

            self.swiat = Swiat(szerokosc, wysokosc)
            # tworzenie okienka
        
            self.window.title("AnimalWorld")
            self.window.geometry("800x600")

            self.canvas = tk.Canvas(self.window, width=550, height=550)
            self.canvas.pack()
            
            self.log_text = tk.Text(self.window, width=50)
            
            def tura(event):
                endOfGame = self.swiat.wykonajTure(event)
                self.rysujSwiat()
                if(endOfGame is True):
                    self.exitgame()
            
            self.window.bind("<Key>", tura)  # oblsluga klawiszy
            self.rysujSwiat()
            self.window.mainloop()
                
            self.window.destroy()
            
        def sysexit():
            sys.exit()

        self.window = tk.Tk()  # plansza
        self.window.resizable(False, False)
        self.window.title("Wymiary planszy")
        self.window.geometry("400x250")

        label_title = tk.Label(self.window, text="AnimalWorld", font=("Arial", 24), fg="blue")  # nazwa gry
        label_title.pack()

        label_szerokosc = tk.Label(self.window, text="Szerokość:")  # scroll na szerokosc
        label_szerokosc.pack()
        scale_szerokosc = tk.Scale(self.window, from_=10, to=20, orient=tk.HORIZONTAL)
        scale_szerokosc.pack()

        label_wysokosc = tk.Label(self.window, text="Wysokość:")  # scroll na wysokosc
        label_wysokosc.pack()
        scale_wysokosc = tk.Scale(self.window, from_=10, to=20, orient=tk.HORIZONTAL)
        scale_wysokosc.pack()

        button_start = tk.Button(self.window, text="Start", command=start_game)  # guzik rozpoczynajacy gre
        button_start.pack()

        button_exit = tk.Button(self.window, text="Zakończ grę", command=sysexit)  # guzik konczacy gre
        button_exit.pack()

        self.window.protocol("WM_DELETE_WINDOW", sysexit)

        self.window.mainloop()

    def exitgame(self):
        messagebox.showinfo("AnimalWorld", "Koniec gry!")
        sys.exit()

    def rysujSwiat(self):
        self.canvas.delete("all")
        self.log_text.delete("1.0", tk.END)
        rozmiar_komorki = int(500/max(self.swiat.m,self.swiat.n))
        margines = 25

        self.obrazki = []  # Lista przechowująca obrazki
        
        for i in range(self.swiat.m):
            for j in range(self.swiat.n):
                x = margines + i * rozmiar_komorki
                y = margines + j * rozmiar_komorki
                isSet = False
                for k in range(self.swiat.iloscOrganizmow):
                    if self.swiat.organizmy[k].isHere(i, j) and self.swiat.czyZyje[k]:
                        isSet = True
                        obrazek = Image.open(self.swiat.organizmy[k].rysowanie())
                        obrazek = obrazek.resize((rozmiar_komorki, rozmiar_komorki), Image.ANTIALIAS)
                        photo = ImageTk.PhotoImage(obrazek)
                        self.canvas.create_image(x, y, anchor=tk.NW, image=photo)
                        self.canvas.create_rectangle(
                            x, y, x + rozmiar_komorki, y + rozmiar_komorki, outline="black", width=2
                        )
                        self.obrazki.append((obrazek, photo))  # Dodanie obiektów do listy obrazków
                if not isSet:
                    tag = f"puste_pole_{i}_{j}"
                    self.canvas.create_rectangle(x, y, x + rozmiar_komorki, y + rozmiar_komorki, fill="white", tags=tag)
                    self.canvas.tag_bind(tag, "<Button-1>", lambda event, i=i, j=j: self.dodawanieOrganizmu(event, i, j))

        for log in self.swiat.logi:
            self.log_text.insert(tk.END, log + "\n")

        self.swiat.logi.clear()

        self.canvas.pack(side=tk.LEFT)
        self.log_text.pack(side=tk.LEFT)
        
        
        szerokosc = 1000 + 2*margines
        wysokosc = 600 + 2*margines

        srodek_x = int(self.window.winfo_screenwidth() / 2 - szerokosc / 2)
        srodek_y = int(self.window.winfo_screenheight() / 2 - wysokosc / 2)

        self.window.geometry(f"{szerokosc}x{wysokosc}+{srodek_x}+{srodek_y}")
        
        self.window.update()
        
        
    def dodawanieOrganizmu(self, event, i, j):
        top = tk.Toplevel()
        top.title("Wybierz organizm")
        
        selected_organism = tk.StringVar()
        selected_organism.set(None)
        
        tk.Radiobutton(top, text="Antylopa", variable=selected_organism, value="Antylopa").pack(anchor='w')
        tk.Radiobutton(top, text="Barszcz Sosnowskiego", variable=selected_organism, value="BarszczSosnowskiego").pack(anchor='w')
        tk.Radiobutton(top, text="Cyber Owca", variable=selected_organism, value="CyberOwca").pack(anchor='w')
        tk.Radiobutton(top, text="Czlowiek", variable=selected_organism, value="Czlowiek").pack(anchor='w')
        tk.Radiobutton(top, text="Guarana", variable=selected_organism, value="Guarana").pack(anchor='w')
        tk.Radiobutton(top, text="Lis", variable=selected_organism, value="Lis").pack(anchor='w')
        tk.Radiobutton(top, text="Mlecz", variable=selected_organism, value="Mlecz").pack(anchor='w')
        tk.Radiobutton(top, text="Owca", variable=selected_organism, value="Owca").pack(anchor='w')
        tk.Radiobutton(top, text="Trawa", variable=selected_organism, value="Trawa").pack(anchor='w')
        tk.Radiobutton(top, text="Wilcze Jagody", variable=selected_organism, value="WilczeJagody").pack(anchor='w')
        tk.Radiobutton(top, text="Wilk", variable=selected_organism, value="Wilk").pack(anchor='w')
        tk.Radiobutton(top, text="Zlow", variable=selected_organism, value="Zlow").pack(anchor='w')
        
        def dodaj_organizm():
            selected_value = selected_organism.get() 
            self.swiat.dodawanieOrganizmu(i, j, selected_value)
            self.rysujSwiat()
            top.destroy()
        
        self.rysujSwiat()
        
        tk.Button(top, text="Dodaj", command=dodaj_organizm).pack()