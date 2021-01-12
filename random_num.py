##To get the value of rand
def seed_LCG(initVal):
    global rand
    rand = initVal

##Use of Linear Congruential Generator Algorithm to generate random number
def lcg():
    a = 11230
    c = 12458
    m = 2**21
    global rand
    rand = (a*rand + c) % m
    return rand / m

seed_LCG(2)

##Ten random numbers are generated
for i in range(10):
    print(lcg())

    
