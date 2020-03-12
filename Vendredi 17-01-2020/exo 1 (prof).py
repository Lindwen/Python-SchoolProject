###########################
#
#   Inititation Python
#   PhrasePython-3
#   BAUDET Alexandre       17/01/20
#
###########################

continuer = True

while continuer:
    ph = input("Entrez une phrase :")
    l = len(ph)
    num_lettre = 1
    for pos in range(l):
        if ph[pos] != ' ':
            print(ph[pos], "Rang :", pos, 'lettre n°', num_lettre)
            num_lettre = num_lettre + 1
        else:
            print(' ')
    rep = input('Voulez-vous rejouer ? (o/n)')
    while rep not in ['o', 'n', 'O', 'N', 'oui', 'non']:
        rep = input('Voulez-vous rejouer ? (o/n)')
    if rep in ['o', 'O', 'oui']:
        continuer = True
    else:
        continuer = False