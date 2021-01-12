def seedLCG(initVal):
    global rand
    rand = initVal

def lcg():
    a = 11230
    c = 12458
    m = 2**21
    global rand
    rand = (a*rand + c) % m
    return rand / m

seedLCG(2)

for i in range(10):
    print(lcg())

    