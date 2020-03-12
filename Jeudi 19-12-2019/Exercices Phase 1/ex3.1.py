# -*- coding: utf8 -*-
##########################################
#
#   Initiation à Python
#   ex3-1
#   A.BAUDET      19/12/2019
#
##########################################

# On demande à l'utilisateur de saisir soit H ou F
sexe = input('Homme ou Femme (H/F) ?')
# Tant que la var sexe est différente de H ou F on repose la question
while (sexe !='H' and sexe !='F'):
    sexe = input('Homme ou Femme (H/F) ?')
# Si la var sexe est égale à H ou F alors on affiche...
print('Au revoir !')