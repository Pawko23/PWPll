import math

def objetosc_szescianu(a):
    return a ** 3

def pole_szescianu(a):
    return 6 * a ** 2

def objetosc_prostopadloscianu(a, b, h):
    return a * b * h

def pole_prostopadloscianu(a, b, h):
    return 2 * (a * b + a * h + b * h)

def objetosc_kuli(r):
    return (4/3) * math.pi * r ** 3

def pole_kuli(r):
    return 4 * math.pi * r ** 2