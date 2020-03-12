# -*- coding: utf8 -*-
##########################################
#
#   Prise en main de Python
#   ex4.2
#   A.BAUDET      19/12/2019
#
##########################################

print('Table de Multiplication')
table = int(input('Quelle table ? '))
nmax = int(input('Quelle nombre max ? '))
print('Table des ', table)
i = 1
while (i <= nmax):
    print(table, ' x', i, ' = ', table*i)
    i += 1
print('Au revoir')