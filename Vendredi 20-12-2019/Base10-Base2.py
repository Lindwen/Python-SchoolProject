# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   Base 10 en Base 2
#   A.BAUDET      20/12/2019
#
##########################################

a_2 = ' '
a_10c = str(input('Nombre en base 10 à transposer en base 2 : '))
a_10 = int(a_10c)

while a_10 != 0:
    r = a_10 % 2
    a_2 = str(r) + a_2
    a_10 = a_10 // 2
print(a_2)
