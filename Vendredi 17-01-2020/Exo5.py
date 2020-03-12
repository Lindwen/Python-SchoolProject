##########################
#
#   Inititation Python
#   BAUDET Alexandre       17/01/20
#
###########################


import unidecode

continuer = True
while continuer:
    sentence = input('Veuillez saisir une phrase, s\'il vous plait : ')
    print('Votre phrase est :', sentence)
    sentence = unidecode.unidecode(sentence)
    char = input('Entrer le caractère que vous souhaitez compter dans la phrase : ')
    count = 0
    while len(char) > 1:
        char = input('Entrer le caractère que vous souhaitez compter dans la phrase : ')
    for c in sentence:
        if c == char:
            count += 1
    print('Le caractère', char, 'a été compté', count, 'fois.')
    rep = input('Voulez-vous rejouer ? (o/n)')
    while rep not in ['o', 'n', 'O', 'N', 'oui', 'non']:
        rep = input('Voulez-vous rejouer ? (o/n)')
    if rep in ['o', 'O', 'oui']:
        continuer = True
    else:
        continuer = False