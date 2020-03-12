# -*- coding: utf8 -*-
##########################################
#
#   Initiation à Python
#   ex2-1
#   A.BAUDET      19/12/2019
#
##########################################

# On demande à l'utilisateur de saisir son nom
nom = input('Quel est votre nom ? ')
# On demande à l'utilisateur de saisir son saxe
sexe = input('Homme ou Femme (H/F) ? ')
# Si la variable sexe est égal à H alors on affiche M. ...
if (sexe == 'H'):
    print('Bonjour M.', nom)
# Sinon on affiche Mme ...
else:
    print('Bonjour Mme', nom)
