from geompy.figury2d import pole_kwadratu, obwod_kwadratu
from geompy.figury3d import objetosc_kuli, pole_kuli

a = 5
print(f"Pole kwadratu o boku {a}: {pole_kwadratu(a)}")
print(f"Obwód kwadratu o boku {a}: {obwod_kwadratu(a)}")

r = 3
print(f"Objętość kuli o promieniu {r}: {objetosc_kuli(r)}")
print(f"Pole powierzchni kuli o promieniu {r}: {pole_kuli(r)}")
