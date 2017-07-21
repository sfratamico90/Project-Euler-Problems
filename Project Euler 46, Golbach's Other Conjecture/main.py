
DOES NOT worker

curbool = True
cur = 5

def primesBelowN(n):
    list = []
    list.append(2)
    for x in range(1, n):
        if (((2**(x-1))% x) == 1):
            list.append(x)
    return list[:]

def golbachCheck(n):
    p = primesBelowN(n)
    for x in range(3,len(p)):
        for y in range(1, int(((float(n)-1)/2)**(.5)) + 1):
            if(p[x] + 2*(y**2) == n):
                return True
    return False
        
while (curbool):
    cur += 1
    if(((2**(cur-1))% cur) == 1 or cur%2 == 0):
        curbool = True
    else:
        curbool = golbachCheck(cur)
        print (cur)

print (cur)