def isPrime(n):
    if (((2**(n-1))% n) == 1):
        return True
    else:
        return False
cur = 3
answer = 0
while (cur < 2000000):
    if (isPrime(cur)):
        answer = answer + cur
        print ("The current answer is ", 2+answer)
        cur = cur + 2
        print ("The current cur is ", cur)
    else:
        cur = cur + 2
        print ("The current cur is ", cur)


print ("THE ANSWER IS ", answer + 2)