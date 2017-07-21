
def divTest(n):
    i = 0
    for x in range(1, int(n/2 + 1)):
        if (float(n)/float(x)==0):
            i += 1
    if (i<500):
        return False
    else:
        return True
it = 1
while (1):
    it += 2
    trn = (it*(it+1))/2
    if (divTest(trn)):
        print (trn)
        break
    else:
        print (trn)
        