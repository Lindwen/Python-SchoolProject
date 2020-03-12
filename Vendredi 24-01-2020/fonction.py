# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   Les fonctions
#   A.BAUDET      24/01/2020
#
##########################################
def consommation(d, v):
    c = (v / d) * 100
    return c


def troncat2(x):
    x = int(x * 100) / 100
    return x


def troncat(x, n):
    n = 10**n
    x = int(x * n) / n
    return x


def arrondin(x, n):
    n = 10**n
    x = x*n
    y = int(x)
    z = x - y
    if z >= 0.5:
        y += 1
    x = y/n
    return x


dist = int(input("distance parcourue en km : "))
vol = float(input("volume d'essence en litre : "))
arrondi = int(input("arrondie voulu : "))
conso = consommation(dist, vol)
conso_tronc = troncat2(conso)
conso_tronc_n = troncat(conso, arrondi)
conso_arrondie = arrondin(conso, arrondi)
print("La consommation est de", conso, 'L aux 100 km.')
print("La consommation est de", conso_tronc, 'L aux 100 km.')
print("La consommation est de", conso_tronc_n, 'L aux 100 km. (a', arrondi, 'chiffres après la ,)')
print("La consommation est de", conso_arrondie, 'L aux 100 km. (arrondie a', arrondi, 'chiffres après la ,)')
