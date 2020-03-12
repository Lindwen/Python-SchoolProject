# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   Base 2 en Base 10
#   A.BAUDET      20/12/2019
#
##########################################

cnbr = input('Nombre en base 2 à transposer en base 10 : ')
length = len(cnbr)
i = 0
calc = 0
scnbr = '0'
tnbr = 0
result = 0
deb = cnbr

while i < length:
    snbr = cnbr[i]
    tnbr = int(snbr)
    result = tnbr * 2 ** (length - i - 1)
    calc = result + calc
    i = i + 1

print(deb, 'en base 2 est', calc, 'en base 10.')
