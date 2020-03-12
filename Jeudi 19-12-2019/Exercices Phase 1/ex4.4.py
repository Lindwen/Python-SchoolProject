# -*- coding: utf8 -*-
##########################################
#
#   Prise en main de Python
#   ex4.4
#   A.BAUDET      19/12/2019
#
##########################################

print('Table de Multiplication')
table = int(input('Quelle table ?'))
print('Table des', table)
for i in range (1, 11):
    print(table, 'x', i, '=', table*i)
print('Au revoir')