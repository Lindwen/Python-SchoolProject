cnbr = "12"
long = len(cnbr)
i = 0
calc = 0
tnbr = 0
result = 0
deb = cnbr

# transposition

while i < long:
    snbr = cnbr[i]
    if snbr == 'A':
        snbr = '10'
    elif snbr == 'B':
        snbr = '11'
    elif snbr == 'C':
        snbr = '12'
    elif snbr == 'D':
        snbr = '13'
    elif snbr == 'E':
        snbr = '14'
    elif snbr == 'F':
        snbr = '15'
    else:
        snbr = snbr

    tnbr = int(snbr)
    result = tnbr * 16 ** (long - i - 1)
    calc = result + calc
    i = i + 1

print(deb, 'en base 16 est', calc, 'en base 10.')
