def findDivs(n):
    divs = []
    for x in range (1,n//2+1):
        if (float(n)%float(x) == 0):
            divs.append(x)
    return divs[:]

def sumSeq(n):
    summ = 0
    for x in range(0,len(n)):
        summ += n[x]
    return summ

def findAbunds(maxx):
    abunList = []
    for x in range(13, maxx):
        if (sumSeq(findDivs(x)) > x):
            abunList.append(x)
            print ("current abundpot: ",x)
        
    return abunList[:]

abundList = findAbunds(28132)

def abundWritable(n):
    for x in range(0,len(abundList)):
        for y in range(0, len(abundList)):
            if (x + y == n):
                return True
    return False

nonAbundSum = 0
for x in range(24, 28132):
    if (abundWritable(x) == False):
        nonAbundSum += x
        print ("current x: ",x)
print (nonAbundSum)
