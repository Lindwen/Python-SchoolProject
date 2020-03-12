# -*- coding: utf8 -*-
##########################################
#
#   Initiation à Python - Synthèse
#   ex1-3
#   A.BAUDET      19/12/2019
#
##########################################

nbO = 5.32
nbJ = float(input('Votre proposition : '))
while (nbJ != nbO):
    if (nbJ > nbO):
        print(nbJ, 'est plus grand que mon nombre')
    else:
        print(nbJ, 'est plus petit que mon nombre')
    nbJ = float(input('Votre proposition : '))
print('Bravo vous avez trouvé')