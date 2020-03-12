#-*-coding: utf-8-*-

# Base 10 vers base 2

# début C

a_2=''
a_10c=input('Nombre en base 10 à transposer :')
a_10=int(a_10c)
deb=a_10

#recherche du nombre

while (a_10 != 0):
    r=a_10%2
    cr=str(r)
    a_2=cr+a_2
    a_10=a_10//2

# affichage

print (deb, 'en base 10 est', a_2, 'en base 2.')



# base 2 vers base 10

# enregistrement des variables

cnbr=a_2
long=len(cnbr)
i=0
calc=0
tnbr=0
result=0
deb=cnbr

# transposition

while (i < long):

    snbr=cnbr[i]
    tnbr=int(snbr)
    result=tnbr*2**(long-i -1)
    calc=result+calc

    i=i+1


#affichage

print (deb, 'en base 2 est', calc, 'en base 10.')


# base 10 vers base 16

# variables

a_16=''
a_10=calc
deb=a_10

#recherche du nombre

while (a_10 != 0):
    r=a_10%16

# changement des valeurs


    if (r>9 and r<16):
        if (r == 10):
            cr='A'
        elif (r == 11):
            cr='B'
        elif (r == 12):
            cr=str(r)
            cr='C'
        elif (r == 13):
            cr='D'
        elif (r == 14):
            cr='E'
        else:
            cr='F'
    else:
        cr=str(r)

# création du résultat
    a_16=cr+a_16
    a_10=a_10//16

# affichage

print (deb, 'en base 10 est', a_16, 'en base 16.')


# base 16 vers base 10

# enregistrement des variables

cnbr=a_16
long=len(cnbr)
i=0
calc=0
tnbr=0
result=0
deb=cnbr

# transposition

while (i < long):

    snbr=cnbr[i]

    # changement des valeurs
    if (snbr == 'A'):
        snbr='10'
    elif (snbr == 'B'):
        snbr='11'
    elif (snbr == 'C'):
        snbr='12'
    elif (snbr == 'D'):
        snbr='13'
    elif (snbr == 'E'):
        snbr='14'
    elif (snbr == 'F'):
        snbr='15'
    else:
        snbr = snbr

    tnbr=int(snbr)
    result=tnbr*16**(long-i -1)
    calc=result+calc

    i=i+1


#affichage

print (deb, 'en base 16 est', calc, 'en base 10.')