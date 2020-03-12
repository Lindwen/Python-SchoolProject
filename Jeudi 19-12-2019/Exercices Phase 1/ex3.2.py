# -*- coding: utf8 -*-
##########################################
#
#   Initiation à Python
#   ex3-2
#   A.BAUDET      19/12/2019
#
##########################################

# On demande à l'utilisateur de saisir soit H soit F
sexe = input('Homme ou femme (H/F) ? ')
# Tant que var sexe est différent de H ou F ....
while (sexe != 'H' and sexe != 'F'):
    sexe = input('Homme ou femme (H/F) ? ')
# Si la var sexe est égale a F alors...
if sexe == 'F':
    print('Au revoir Madame !')
# Sinon...
else:
    print('Au revoir Monsieur !')