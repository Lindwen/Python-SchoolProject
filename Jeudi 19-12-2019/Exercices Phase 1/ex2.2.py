# -*- coding: utf8 -*-
##########################################
#
#   Initiation à Python
#   ex2-2
#   A.BAUDET      19/12/2019
#
##########################################

# On demande à l'utilisateur de saisir une note
note = int(input('Votre note ? '))
# Si la note est inférieure à 8 alors...
if (note < 8):
    print('Pas terrible !')
# Sinon Si la note est inférieure à 12 alors...
elif (note < 12):
    print('Moyen !')
# Sinon Si la note est inférieure ou égale à 15 alors...
elif (note <=15):
    print('Pas mal !')
# Sinon ...
else:
    print('Très bien !')