panDigis = set()

def isPandigital(n):
    sum = 0
    for x in range (1, len(str(n))+1):
        sum += 1 if str(x) in str(n) else 0
    return True if sum == len(str(n)) else False

def findDivs(n):
    divs = []
    for x in range (1,n//2+1):
        if (float(n)%float(x) == 0):
            divs.append(x)
    return divs[:]

for x in range (1000000):
    if (isPandigital(x)):
        for y in findDivs(x):
            if (isPandigital(int(str(y) + str(x/y) + str(x)))):
                panDigis.add(x)
                print ("new pan!: ", x)

def sumSeq(n):
    prod = 0
    for x in range(0,len(n)):
        prod += n[x]
    return prod

print (sumSeq(panDigis))
