# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   ex1
#   A.BAUDET      19/12/2019
#
##########################################

def SommeImpair(n):
    s = 0
    for i in range(1, n+1,2):
        s += i
    return(s)


if __name__ == '__main__':
    n = int(input("Entrez un nombre: "))
    somme = SommeImpair(n)
    print("La somme de est: {}".format(somme))