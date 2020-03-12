# -*- coding: utf8 -*-
##########################################
#
#   Exercices en Python
#   ex1
#   A.BAUDET      19/12/2019
#
##########################################

def main(n):
    s = 0
    if n % 2 != 0:
        param = n+2
    else:
        param = n-1
    for i in range(1, param):
        if i % 2 == 0:
            print(i)
            s += i
    print("La somme de est: {}".format(s))


if __name__ == '__main__':
    n = int(input("Entrez un nombre: "))
    main(n)
