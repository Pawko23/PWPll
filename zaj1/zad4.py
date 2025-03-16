class Ksiazka:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania

    def opis(self):
        return f"Książka ma tytuł '{self.tytul}'. Napisana przez {self.autor} i została wydana w roku {self.rok_wydania}"
    
ksiazka1 = Ksiazka("Atomic Habits", "James Clear", 2015)
print(ksiazka1.opis())

class Ebook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, rozmiar_pliku):
        super().__init__(tytul, autor, rok_wydania)
        self.rozmiar_pliku = rozmiar_pliku

    def opis(self):
        return f"{super().opis()}. Rozmiar pliku Ebooka to {self.rozmiar_pliku}MB"
    
ebook = Ebook("Atomic Habits", "James Clear", 2015, 1024)
print(ebook.opis())

class Audiobook(Ksiazka):
    def __init__(self, tytul, autor, rok_wydania, czas_trwania):
        super().__init__(tytul, autor, rok_wydania)
        self.czas_trwania = czas_trwania
    
    def opis(self):
        return f"{super().opis()}. Czas trwania to {self.czas_trwania} minut"
    
audiobook = Audiobook("Atomic Habits", "James Clear", 2015, 3600)
print(audiobook.opis())