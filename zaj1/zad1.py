import json

class AplikacjaMobilna:

    liczba_pobran = 0

    def __init__(self, nazwa, wersja):
        self.nazwa = nazwa
        self.wersja = wersja

    @classmethod
    def nowe_pobranie(cls):
        cls.liczba_pobran += 1

    @classmethod
    def ile_pobran(cls):
        return cls.liczba_pobran

    @classmethod
    def z_json(cls, nazwa_pliku):
        try:
            with open(nazwa_pliku, "r", encoding="utf-8") as plik:
                dane = json.load(plik)
                return cls(dane["nazwa"], dane["wersja"])
        except (FileNotFoundError, KeyError, json.JSONDecodeError):
            print("Błąd")
            return None


app1 = AplikacjaMobilna("Test App", "1.0")
print(app1.nazwa, app1.wersja)

AplikacjaMobilna.nowe_pobranie()
AplikacjaMobilna.nowe_pobranie()
print(AplikacjaMobilna.ile_pobran())

app_z_pliku = AplikacjaMobilna.z_json("file.json")
if app_z_pliku:
    print(app_z_pliku.nazwa, app_z_pliku.wersja)
