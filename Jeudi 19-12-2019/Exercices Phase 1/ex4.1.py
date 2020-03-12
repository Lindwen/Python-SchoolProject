# -*- coding: utf8 -*-
##########################################
#
#   Prise en main de Python
#   ex4.1
#   A.BAUDET      19/12/2019
#
##########################################

print('Table de Multiplication')
table = int(input('Quelle table ?'))
print('Table des ', table)
i = 1
while (i < 11):
    print(table, ' x', i, ' = ', table*i)
    i = i+1
    # i += 1
print('Au revoir')