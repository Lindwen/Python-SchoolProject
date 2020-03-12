# -*- coding: utf8 -*-
##########################################
#
#   Initiation à Python - Synthèse2
#   ex1-3
#   A.BAUDET      19/12/2019
#
##########################################

# Loterie

import random

coup = 1
mise = 1
depense = 1
gagne = 'non'
while gagne == 'non' and depense < 200:
    boule = random.randint(9, 49)
    premier = 'oui'
    i = 2
    while i < boule and premier == 'oui':
        if (boule % i) == 0:
            premier = 'non'
        i += 1
    if premier == 'oui':
        print(boule, 'est le premier, au coup n°', coup, 'le gain total est de ', 3 * mise - depense)
        gagne = 'oui'
    else:
        print('coup n°', coup, ' ', boule, 'n\'est pas premier')
        mise = 2 * mise
        coup += 1
        depense = depense + mise
if gagne == 'non':
    print('Le joueur a perdu :', depense - mise, ' Euros')
