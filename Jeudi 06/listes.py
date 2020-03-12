li = [1,2,3,1,2,3,1,2,3]
print(li)
nb = li.count(1)
while nb > 0:
    li.remove(1)
    nb -= 1
print(li)


'''
li = [1,2,3,1,2,3,1,2,3]
print(li)
nb = li.count(1)
i = 0
while i < nb:
    li.remove(1)
    i += 1
print(li)
'''