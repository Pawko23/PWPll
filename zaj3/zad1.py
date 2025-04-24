"""Moduł zarządzający biblioteką i książkami.

Zawiera klasy:
- Ksiazka: reprezentuje książkę z tytułem, autorem i statusem dostępności.
- Biblioteka: przechowuje książki i pozwala na ich wypożyczanie i zwracanie.
"""

class Ksiazka: # pylint: disable=too-few-public-methods
    """Reprezentuje książkę w bibliotece."""
    def __init__(self, tytul, autor, dostepna=True):
        """Inicjalizuje obiekt książki."""
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna


class Biblioteka:
    """Reprezentuje bibliotekę przechowującą książki."""
    def __init__(self):
        """Tworzy pustą listę książek w bibliotece."""
        self.lista_ksiazek = []

    def dodaj_ksiazke(self, ksiazka):
        """Dodaje książkę do biblioteki."""
        self.lista_ksiazek.append(ksiazka)

    def wypozycz_ksiazke(self, tytul):
        """Wypożycza książkę, jeśli jest dostępna."""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                if ksiazka.dostepna:
                    ksiazka.dostepna = False
                    return f"Wypozyczono: {tytul}"
            return f"Brak ksiazki: {tytul}"

    def zwroc_ksiazke(self, tytul):
        """Zwraca książkę do biblioteki."""
        for ksiazka in self.lista_ksiazek:
            if ksiazka.Tytul == tytul:
                ksiazka.dostepna = True
                return f"Zwrocono: {tytul}"
        return f"Nie nalezy do biblioteki: {tytul}"

    def dostepne_ksiazki(self):
        """Zwraca listę dostępnych książek."""
        dostepne = []
        for ksiazka in self.lista_ksiazek:
            if ksiazka.dostepna:
                dostepne.append(ksiazka.Tytul)
        return dostepne


def main():
    """Test programu"""
    biblioteka = Biblioteka()
    biblioteka.dodaj_ksiazke(Ksiazka("Wiedzmin", "Sapkowski"))
    biblioteka.dodaj_ksiazke(Ksiazka("Solaris", "Lem"))
    biblioteka.dodaj_ksiazke(Ksiazka("Lalka", "Prus", False))

    print(biblioteka.wypozycz_ksiazke("Solaris"))
    print(biblioteka.wypozycz_ksiazke("Lalka"))
    print(biblioteka.zwroc_ksiazke("Lalka"))
    print("Dostepne ksiazki: ", biblioteka.dostepne_ksiazki())


main()
