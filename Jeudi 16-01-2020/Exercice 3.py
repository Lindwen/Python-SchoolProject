###########################
#
#   Inititation Python
#   PhrasePython-3
#   BAUDET Alexandre       16/01/20
#
###########################

continuer = True

while continuer:
    ph = input("Entrez une phrase :")
    l = len(ph)
    pos = 0
    rang = 0
    while pos < l:
        if ph[pos] != ' ' and ph[pos] != '\'':
            print(ph[pos], "Rang :", rang)
            rang += 1
        pos += 1
    rep = input('Voulez-vous rejouer ? (o/n)')
    while rep not in ['o', 'n', 'O', 'N', 'oui', 'non']:
        rep = input('Voulez-vous rejouer ? (o/n)')
    if rep in ['o', 'O', 'oui']:
        continuer = True
    else:
        continuer = False