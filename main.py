from tkinter import *
from tkinter import messagebox
from Belepes_Modul import *
from Jelszo import  *
from AAnimal_Modul import *


#felhasznalónév= Admin
#jelszó=Admin123


def belepes():
    def ok_gomb_kezelese():
        dolgozo.felhasznalo_neve = f_nev.get()
        dolgozo.felhasznalo_jelszava = f_jelszo.get()
        if f_nev.get() == "" or f_jelszo.get() == "":
            messagebox.showinfo("Hiba", "Valamelyik mező üres", parent=be_ablak)
        elif " " in f_nev.get():
            messagebox.showinfo("Hiba", "Szóközt használt a felhasználónévben!", parent=be_ablak)
        elif dolgozo.felhasznalo_ell():
            messagebox.showinfo("Belépés", "Sikeres belépés!")
        elif dolgozo.felhasznalo_ell():
            messagebox.showinfo("Belépés", "Belépés megtagadva!")
        elif not dolgozo.jelszo_vizsgalata(8):
            messagebox.showinfo("Hiba", "Nem megfelelő a jelszó!", parent=be_ablak)
        else:
            be_ablak.destroy()


    def reg_kerese():
        be_ablak.destroy()
        regisztracio()

    be_ablak = Tk()
    be_ablak.title("Állatorvosi nyilvántartás beléptető oldal")
    be_ablak.geometry("400x200")

    f_nev_cimke = Label(be_ablak, text="Felhasználó név:")
    f_jelszo_cimke = Label(be_ablak, text="Jelszó:")

    f_nev = StringVar()
    f_nev.set("")
    f_nev_be = Entry(be_ablak, textvariable=f_nev, width=20)
    f_jelszo = StringVar()
    f_jelszo.set("")
    f_jelszo_be = Entry(be_ablak, textvariable=f_jelszo, width=20)

    ok_gomb = Button(be_ablak, text="OK", command=ok_gomb_kezelese, width=10)
    reg_gomb = Button(be_ablak, text="Regisztráció", command=reg_kerese)

    f_nev_cimke.grid(row=0, column=0, sticky="E", padx=15)
    f_nev_be.grid(row=0, column=1, padx=15)
    f_jelszo_cimke.grid(row=1, column=0, sticky="E", padx=15)
    f_jelszo_be.grid(row=1, column=1)
    reg_gomb.grid(row=2, column=0, padx=15)
    ok_gomb.grid(row=2, column=1, pady=15)

    be_ablak.mainloop()

def regisztracio():

    def ok_gomb_kezelese():
        dolgozo.felhasznalo_neve = f_nev.get()
        dolgozo.felhasznalo_jelszava = f_jelszo.get()
        if f_nev.get() == "" or f_jelszo.get() == "" :
            messagebox.showinfo("Hiba", "Valamelyik mező üres", parent=reg_ablak)
        elif f_jelszo.get() != f_jelszo2.get():
            messagebox.showinfo("Hiba", "Nem azonosak a jelszavak", parent=reg_ablak)
        elif " " in f_nev.get():
            messagebox.showinfo("Hiba", "Szóközt használt a felhasználónévben!", parent=reg_ablak)
        elif not dolgozo.jelszo_vizsgalata(8):
            messagebox.showinfo("Hiba", "Nem megfelelő a jelszó!", parent=reg_ablak)
        else:
            reg_ablak.destroy()
            dolgozo.tarolas()

    def jelszo_gen():
        dolgozo.jelszo_generalasa()
        f_jelszo.set(dolgozo.felhasznalo_jelszava)
        f_jelszo2.set(dolgozo.felhasznalo_jelszava)

    reg_ablak = Tk()
    reg_ablak.title("Regisztráció")

    f_nev_cimke = Label(reg_ablak, text="Felhasználó név:")
    f_jelszo_cimke =Label(reg_ablak, text="Jelszó:")
    f_jelszo2_cimke = Label(reg_ablak, text="Jelszó újra:")

    ok_gomb = Button(reg_ablak, text="OK", command=ok_gomb_kezelese, width=10)
    jelszo_gen_gomb = Button(reg_ablak, text="Jelszó generálása", command=jelszo_gen)

    f_nev = StringVar()
    f_nev.set("")
    f_nev_be = Entry(reg_ablak, textvariable=f_nev, width=20)
    f_jelszo = StringVar()
    f_jelszo.set("")
    f_jelszo_be = Entry(reg_ablak, textvariable=f_jelszo, width=20)
    f_jelszo2 = StringVar()
    f_jelszo2.set("")
    f_jelszo2_be = Entry(reg_ablak, textvariable=f_jelszo2, width=20)

    f_nev_cimke.grid(row=0, column=0, sticky="E", padx=15)
    f_nev_be.grid(row=0, column=1)
    f_jelszo_cimke.grid(row=1, column=0, sticky="E", padx=15)
    f_jelszo_be.grid(row=1, column=1)
    jelszo_gen_gomb.grid(row=1, column=2, padx=15)
    f_jelszo2_cimke.grid(row=2, column=0, sticky="E", padx=15)
    f_jelszo2_be.grid(row=2, column=1)
    ok_gomb.grid(row=3, column=1, pady=15, columnspan=2)


    reg_ablak.mainloop()

def uj_allat():
    window_ablak = Tk()
    window_ablak.title("Állat rögzítése")
    window_ablak.geometry("400x200")
    """Új állat hozzáadása"""
    animal.create_animal_form(window_ablak)
    window_ablak=Tk()
    window_ablak.destroy()

def allatok_lista():
    new_window = Tk()
    new_window.geometry("400x200")
    new_window.title("Állatok Listája")
    """Állatok listázása"""
    szamlalo=1
    for i in animal.animals:
        tk.Label(new_window,
                    text=f"{szamlalo}. {i['nev']} - {i['fajta']}- {i['gazda']}- {i['elerhetoseg']}").pack()
        szamlalo +=1

def uj_kezeles():
    pass

animal = AAnimal()
dolgozo = Felhasznalo()

belepes()

app = Tk()
app.title("Állatorvosi nyilvántartás")
app.geometry("600x400")

menulista = Menu(app)

allatok = Menu(menulista)
allatok.add_command(label="Új állat hozzáadása", command=uj_allat)
allatok.add_command(label="Állatok listázása", command=allatok_lista)
menulista.add_cascade(label="Állatok", menu=allatok)

app.config(menu=menulista)

# Main program

app.mainloop()














