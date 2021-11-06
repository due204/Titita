from string import hexdigits
from random import choice

passv = []
passd = []
passf = []


def random_car(x):
    return "".join(choice(hexdigits) for x in range(x))


def encriptar(x):
    cnt = 1
    for i in x:
        passv.append(random_car(cnt) + i)
        cnt += 1
    return "".join(passv)


def decriptar(x):
    cont1 = 0
    cont2 = 2
    cont3 = 2
    passd = list(x)
    while True:
        if cont2 <= len(passd):
            passf.append(passd[cont1:cont2].pop())
            cont3 += 1
            cont1 = cont2
            cont2 = cont2 + cont3
        else:
            break
    return "".join(passf)
