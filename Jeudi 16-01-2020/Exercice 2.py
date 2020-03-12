###########################
#
#   Inititation Python
#   PhrasePython-2
#   BAUDET Alexandre      16/01/20
#
###########################

ph = input("Entrez une phrase :")
l = len(ph)
pos = 0

while pos < l:
    print(ph[pos], "Rang :", pos)
    pos = pos + 1
