# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   Base 10 en Base 16
#   A.BAUDET      20/12/2019
#
##########################################

a_16 = ' '
a_10c = input('Nombre en base 10 à transposer en base 16 : ')
a_10 = int(a_10c)
r = 0

while a_10 != 0:
    r = a_10 % 16
    if r == 10:
        r = 'A'
    elif r == 11:
        r = 'B'
    elif r == 12:
        r = 'C'
    elif r == 13:
        r = 'D'
    elif r == 14:
        r = 'E'
    elif r == 15:
        r = 'F'
    a_16 = str(r) + a_16
    a_10 = a_10 // 16
print(a_16)
