def findDivs(n):
    divs = []
    for x in range (1,n//2+1):
        if (float(n)%float(x) == 0):
            divs.append(x)
            print ("new div! ", x)
    return divs[:]
def primesBelowN(n):
    list = []
    list.append(2)
    for x in range(1, n):
        if (((2**(x-1))% x) == 1):
            list.append(x)
    return list[:]

def findPSR(n, m):
    PSRpot = 0
    sqrt = float(m)**(.5)
    for x in range(0,len(n)):
        if (n[x] < sqrt):
            PSRpot = n[x]
            print ("current PSRpot is ", PSRpot)
    return PSRpot

def prodSeq(n):
    prod = 1
    for x in range(0,len(n)):
        prod *= n[x]
    return prod

print (findPSR(findDivs(prodSeq(primesBelowN(190))),prodSeq(primesBelowN(190))))