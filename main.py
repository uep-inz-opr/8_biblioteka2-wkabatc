class Biblioteka:
    def __init__(self):
        self.__ksiazki = {}
        self.__czytelnicy = {}
    def dodaj(self, tytul, autor, rok_wydania):
        try:
            ksiazka = self.__ksiazki[tytul]
        except KeyError:
            ksiazka = Ksiazka(tytul, autor)
            self.__ksiazki[tytul] = ksiazka
        ksiazka.egzemplarze.append(Egzemplarz(rok_wydania, ksiazka))
        return True
    def dostepne_egz(self, tytul):
        try:
            return [ egz for egz in self.__ksiazki[tytul].egzemplarze if not egz.wypozyczony ]
        except KeyError:
            return []
    def __pobierz_czytelnika(self, nazwisko):
        try:
            return self.__czytelnicy[nazwisko]
        except KeyError:
            nowy = Czytelnik(nazwisko)
            self.__czytelnicy[nazwisko] = nowy
            return nowy
    def wypozycz(self, nazwisko, tytul):
        try:
            egzemplarz = self.dostepne_egz(tytul)[0]
            czytelnik = self.__pobierz_czytelnika(nazwisko)
            a= (czytelnik.wypozycz(egzemplarz))
            print(a)
        except IndexError:
            return False
    def oddaj(self, nazwisko, tytul):
        czytelnik = self.__pobierz_czytelnika(nazwisko)
        b=czytelnik.oddaj(tytul)
        print(b)

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        self.egzemplarze = []

class Egzemplarz:
    def __init__(self, rok_wydania, ksiazka):
        self.rok_wydania = rok_wydania
        self.ksiazka = ksiazka
        self.wypozyczony = False

class Czytelnik:
    limit = 3
    def __init__(self, nazwisko):
        self.nazwisko = nazwisko
        self.wypozyczone = {}
    def wypozycz(self, egzemplarz):
        tytul = egzemplarz.ksiazka.tytul
        if Czytelnik.limit > len(self.wypozyczone) and tytul not in self.wypozyczone.keys():
            egzemplarz.wypozyczony = True
            self.wypozyczone[tytul] = egzemplarz
            return True
        else:
            return False
    def oddaj(self, tytul):
        try:
            self.wypozyczone.pop(tytul).wypozyczony = False
            return True
        except KeyError:
            return False

biblioteka = Biblioteka()
czynnosci=[]
for t in range(int(input())):
    czynnosci.append(eval(input()))

for i in czynnosci:
    if i[0].strip() == "dodaj":
        a = biblioteka.dodaj(i[1].strip(), i[2].strip(), i[3])
    if i[0].strip() == "wypozycz":
        a = biblioteka.wypozycz(i[1].strip(), i[2].strip())
    if i[0].strip() == "oddaj":
        a = biblioteka.oddaj(i[1].strip(), i[2].strip())
    if (a != None):
        print(a)