Adamkó Anita_N6NUDG
Szkrip nyelvek beadandó projekt feladat
Állatorvosi nyilvántartó rendszer
Egy állatrovosi nyilvántartó rendszert fejlesztettem, az órai dolgozói nyilvántartás alapján. 
Van egy bejelentkező oldal, amin keresztül be lehet lépni a rendszerbe, illetve egy regisztrációs felület is rendelkezésre áll.
A sikeres bejelentkezés után, a nyilvántartó rendszerben lehetőség van új állatok felvételére, az állatokhoz a gazdákat is hozzá lehet rendelni elérhetőséggel együtt.
A sikeres állat felvétele után lehetőség van a felvett állatok listázására, ahol szintén gazdák nevével és elérhetőségével szerepelnek az állatok.
A következő modulok találhatók a projektben: AAnimal és Belepes modulok illetve van még egy Jelszo fájl is.
A következő függvények találhatóak meg az AAnimal modulban: 
          create_animal_form (ebben vannak beállítva a front elemei) 
          save_animal(itt az új állatok definiálása található) 
          show_animal(itt az állatok listázása szerepel)
A következő függvények találhatóak meg a Belepes modulban:
          felhasznalonev(felhasználónév bekérése)
          jelszo_ellenorzese(jelszó ellenőrzése)
          regisztracio(jelszó tartalmának a vizsgálata)
          beleptetes(felhasználó és jelszó ellenőrzése, ha szerepel a listában akkor beléphet, ha nem akkor megtagadjuk a belépést)
Jelszó fájl tartalma:
          A regisztrációs felületen lehetőség van jelszó generálására,ennek a lekezelés található meg itt.
          Illetve szintén a jelszó vizsgálatára vonatkozó adatok.
A program indítása a main.py fájlból történik, ez a fájl tartalmazza  a front részeket.
