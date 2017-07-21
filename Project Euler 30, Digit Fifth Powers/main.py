powerDigs = []

#to find all sum of all powerDigs of length n and power n plug in n for both paramters
def powerSumDig(n, m):
    potSum = 0
    for x in range(0, len(str(n))):
        potSum += int(str(n)[x])**m
    return True if potSum == n else False

def sumSeq(n):
    summ = 0
    for x in range(0,len(n)):
        summ += n[x]
    return summ

for x in range(3, 1000000):
    if (powerSumDig(x, 5)):
        powerDigs.append(x)
        
print (sumSeq(powerDigs))