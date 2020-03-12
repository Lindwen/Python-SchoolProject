# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   Fonctions de bases
#   A.BAUDET      31/01/2020
#
##########################################
def base10a2(x10):
    """
    x10 est un nombre en base 10
    la fonction renvoie une chaine de caractère :
    le nombre x10 ecrit en base 2
    """
    x2 = ''
    while (x10 != 0):
        r = x10 % 2
        cr = str(r)
        x2 = cr + x2
        x10 = x10 // 2
    return(x2)


def base2a10(x2):
    """
    x2 est un nombre en base 2
    la fonction renvoie une chaine de caractère :
    le nombre x2 ecrit en base 10
    """
    long = len(x2)
    i = 0
    x10 = 0
    while (i < long):
        snbr = x2[i]
        result = int(snbr) * 2 ** (long-i -1)
        x10 = result + x10
        i = i + 1
    return(x10)


def base10a16(x10):
    """
    x10 est un nombre en base 10
    la fonction renvoie une chaine de caractère :
    le nombre x10 ecrit en base 16
    """
    x16 = ''
    while (x10 != 0):
        r = x10 % 16
        if (r > 9 and r < 16):
            if (r == 10):
                cr = 'A'
            elif (r == 11):
                cr = 'B'
            elif (r == 12):
                cr = 'C'
            elif (r == 13):
                cr = 'D'
            elif (r == 14):
                cr = 'E'
            else:
                cr = 'F'
        else:
            cr = str(r)
        x16 = cr + x16
        x10 = x10 // 16
    return(x16)


def base16a10(x16):
    """
    x16 est un nombre en base 16
    la fonction renvoie une chaine de caractère :
    le nombre x16 ecrit en base 10
    """
    long = len(x16)
    i = 0
    x10 = 0
    while (i < long):
        snbr = x16[i]
        if (snbr == 'A'):
            snbr = '10'
        elif (snbr == 'B'):
            snbr = '11'
        elif (snbr == 'C'):
            snbr = '12'
        elif (snbr == 'D'):
            snbr = '13'
        elif (snbr == 'E'):
            snbr = '14'
        elif (snbr == 'F'):
            snbr = '15'
        else:
            snbr = snbr
        result = int(snbr) * 16 ** (long-i -1)
        x10 = result + x10
        i = i + 1
    return(x10)


## main ##
nb10 = int(input("Quel est votre nombre en base 10 ? "))
print("\n\n\n\n\n\n\n")
print("\n+-------------- Réultats --------------+\n")
nb2 = base10a2(nb10)
print(nb10, 'en base 10 =', nb2, 'en base 2.')
nb10_2 = base2a10(nb2)
print(nb2, 'en base 2 =', nb10_2, 'en base 1O.')
nb16 = base10a16(nb10)
print(nb10, 'en base 10 =', nb16, 'en base 16.')
nb10_16 = base16a10(nb16)
print(nb16, 'en base 16 =', nb10_16, 'en base 10.')
print("\n+--------------------------------------+\n")