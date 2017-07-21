def sumSeq(n):
    prod = 0
    for x in range(0,len(n)):
        prod += int(n[x])
    return prod

def factorial(n):
    return n*factorial(n-1) if n > 0 else 1

print (sumSeq(str(factorial(100))))