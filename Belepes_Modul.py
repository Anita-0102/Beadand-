
def felhasznalonev():
    _felhasznalo_neve = input("Kérem adja meg a felhasználó nevet ")
    while " " in _felhasznalo_neve:
        print("Érvénytelen felhasználónév!")
        if " " in _felhasznalo_neve:
            print("Szóközt használtál a felhasználó névben!")
        _felhasznalo_neve = input("Kérem a felhasználó nevet:")
    return _felhasznalo_neve


def jelszo_ellenorzese(jelszo):
    ok = False
    proba = 0
    while True:
        jelszo2 = input("Kérem ismét a jelszót: ")
        if jelszo == jelszo2:
            ok = True
            break
        else:
            proba += 1
            print("Nem megfelelő a jelszó!")
            if proba == 3:
                break
    return ok


def regisztracio():
    def jelszo_bekerese(hosszusag):
        def hossz(_jelszo, min_hossz):
            ok = True
            if len(_jelszo) < min_hossz:
                ok = False
            return ok

        def szamjegyek(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isnumeric():
                    ok = True
                    break
            return ok

        def kisbetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.islower():
                    ok = True
                    break
            return ok

        def nagybetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isupper():
                    ok = True
                    break
            return ok

        jelszo = input("Kérem a jelszót: ")
        while not hossz(jelszo, hosszusag) or not szamjegyek(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo) or " " in jelszo:
            print("Nem megfelelő a jelszó!")
            jelszo = input("Kérem a jelszót: ")
        return jelszo

    def rogtites(email, jelszo):
        with open('dolgozok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(email + ";" + jelszo + "\n")

    felhasznalo_neve = felhasznalonev()
    felhasznalo_jelszo = jelszo_bekerese(8)
    ok = jelszo_ellenorzese(felhasznalo_jelszo)
    if ok:
        rogtites(felhasznalo_neve, felhasznalo_jelszo)
    return ok


def beleptetes():
    def felhasznalo():
        jelszo = False
        nev = felhasznalonev()
        with open('dolgozok.txt', 'r', encoding='utf-8') as fajl:
            for sor in fajl:
                felhasznaloi_adatok = sor.strip().split(";")
                if felhasznaloi_adatok[0] == nev:
                    jelszo = felhasznaloi_adatok[1]
                    break
        return jelszo

    def jelszoellenorzes(_jelszo):
        ok = False
        if jelszo_ellenorzese(_jelszo):
            ok = True
        return ok

    jelszo = felhasznalo()
    if not jelszo:
        print("Nem vagy regisztrált felhasználó!")
    else:
        if jelszoellenorzes(jelszo):
            print("Sikeres belépés!")
        else:
            print("Belépés megtagadva!")
