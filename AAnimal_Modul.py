import tkinter as tk
class AAnimal:
    def __init__(self):
        self.animals = []

    def create_animal_form(self, window):

        tk.Label(window, text="Állat neve:").grid(row=0, column=0)
        tk.Label(window, text="Fajta:").grid(row=1, column=0)
        tk.Label(window, text="Gazda neve:").grid(row=2, column=0)
        tk.Label(window, text="Gazda elérhetősége:").grid(row=3, column=0)

        nev_entry = tk.Entry(window)
        fajta_entry = tk.Entry(window)
        gazda_entry = tk.Entry(window)
        elerhetoseg_entry=tk.Entry(window)

        nev_entry.grid(row=0, column=1)
        fajta_entry.grid(row=1, column=1)
        gazda_entry.grid(row=2, column=1)
        elerhetoseg_entry.grid(row=3, column=1)


        def save_animal():
            """Új állat hozzáadása"""
            nev = nev_entry.get()
            fajta = fajta_entry.get()
            gazda =gazda_entry.get()
            elerhetoseg =elerhetoseg_entry.get()
            self.animals.append({"nev": nev, "fajta": fajta, "gazda": gazda,"elerhetoseg": elerhetoseg})
            print(f"Új állat hozzáadva: {nev} ({fajta} {gazda} {elerhetoseg})")
            window.destroy()

        save_button = tk.Button(window, text="Felvétel", command=save_animal)
        save_button.grid(row=4, column=1, pady=15, columnspan=2)

    def show_animals(self, new_window):
        """Állatok listázása"""
        for i, animal in enumerate(self.animals):
            tk.Label(new_window, text=f"{i+1}. {animal['nev']} - {animal['fajta']}- {animal['gazda']}- {animal['elerhetoseg']}").pack()
