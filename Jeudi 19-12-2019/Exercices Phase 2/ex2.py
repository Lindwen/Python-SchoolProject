# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   ex1
#   A.BAUDET      19/12/2019
#
##########################################

sentence = input('Saisissez votre phrase : ')
sentence = sentence + ' '

length = len(sentence)
i = 0
mot = ''
while i < length:
    if sentence[i] == ' ' or sentence[i] == "'":
        print(mot)
        mot = ''
    else:
        mot = mot + sentence[i]

    i += 1
