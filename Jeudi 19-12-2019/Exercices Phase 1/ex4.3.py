# -*- coding: utf8 -*-
##########################################
#
#   Prise en main de Python
#   ex4.3
#   A.BAUDET      19/12/2019
#
##########################################

rep = 'O'
print('Table de Multiplication')
while (rep == 'O'):
    table = int(input('Quelle table ? '))
    print('Table des', table)
    i = 1
    while (i < 11):
        print(table, 'x', i, '=', table*i)
        i = i+1
    rep = input('Une autre table ? (O/N) ')
print('Au revoir')