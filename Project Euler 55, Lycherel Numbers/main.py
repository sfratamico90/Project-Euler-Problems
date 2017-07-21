def isPali(n):
    length = len(str(n))
    for x in range(0,length):
        if(str(n)[x] != str(n)[length - 1 - x]):
            return False
    return True

def reverseNum(n):
    return int(str(n)[::-1])

def isLycherell(n):
    curnum = n
    for x in range(1,50):
        if (isPali(reverseNum(curnum)+curnum)):
            return False
        else:
            curnum += reverseNum(curnum)
    return True

count = 0
for x in range(1, 10001):
    if(isLycherell(x)):
        count += 1

print (count)
