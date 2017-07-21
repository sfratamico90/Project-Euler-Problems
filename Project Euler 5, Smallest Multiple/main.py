i = 0
def divisCheck(n):
    for x in range(1,21):
        if (n%float(x) != 0):
            return False
    return True

while (1):
    i +=20
    if (divisCheck(i) == True):
        break
    else:
        print (i)
print (i)