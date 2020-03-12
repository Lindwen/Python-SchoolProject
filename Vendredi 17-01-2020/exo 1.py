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
    rang = 0
    for c in ph:
        if c != ' ' and c != '\'':
            print(c, "Rang :", rang)
            rang += 1
    rep = input('Voulez-vous rejouer ? (o/n)')
    while rep not in ['o', 'n', 'O', 'N', 'oui', 'non']:
        rep = input('Voulez-vous rejouer ? (o/n)')
    if rep in ['o', 'O', 'oui']:
        continuer = True
    else:
        continuer = False