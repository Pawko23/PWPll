class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko}"
    

person1 = Osoba("John", "Paul", 88)
test = person1.przedstaw_sie()
print(test)

class Pracownik(Osoba):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek)
        self.stanowisko = stanowisko
        self.pensja = pensja

    def info_o_pracy(self):
        return f"{self.przedstaw_sie()}. Pracuję jako {self.stanowisko}, zarabiam {self.pensja}zl"
    
pracownik = Pracownik("Jarek", "Czerwonka", 41, "Luzik Arbuzik Manager", 17000)
print(pracownik.info_o_pracy())

class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super.__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = []


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, wiek, stanowisko, pensja):
        super().__init__(imie, nazwisko, wiek, stanowisko, pensja)
        self.zespol = []

    def przedstaw_sie(self):
        return f"{super().przedstaw_sie()}. Moj zespol liczy {len(self.zespol)} osob."
    
    def dodaj_do_zespolu(self, pracownik):
        self.zespol.append(pracownik)
        

manager = Manager("Jan", "Kowalski", 35, "Manager", 50000)

pracownik1 = Pracownik("Anna", "Nowak", 30, "Programista", 8000)
pracownik2 = Pracownik("Piotr", "Wiśniewski", 35, "Tester", 7000)
manager.dodaj_do_zespolu(pracownik1)
manager.dodaj_do_zespolu(pracownik2)
print(manager.info_o_pracy())