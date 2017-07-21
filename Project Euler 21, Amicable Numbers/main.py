def findDivisors(n):
    divisorList = []
    for x in range(1, n//2 + 1):
        m = float(n)
        y = float(x)
        if((m/y)%1 == float(1) & m%y == float(0)):
            divisorList.append(m//y)
            
def sumList(L):
    summ = 0
    for x in range(0, len(L)):
        summ += L[x]
    return sum
print (sum(findDivisors(100)))