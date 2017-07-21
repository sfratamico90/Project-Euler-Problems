maxlength = 1
curmain = 500000
maxcorres = 0
def cal(n):
    if (n%2 == 0):
        return n/2
    else:
        return (3*n+1)

def chain(n):
    length = 1
    cur = n
    while (cur > 1):
        cur = cal(cur)
        length += 1
    return length

def comp(n):
    if (n > maxlength):
        return n
    else:
        return maxlength

def cORP(n):
    if (n > maxlength):
        return curmain
    else:
        return maxcorres
while (curmain < 1000000):
    newchain = chain(curmain)
    maxcorres = cORP(newchain)
    maxlength = comp(newchain)
    print ("Current maxlength: ", maxlength)
    print ("Current curmain :", curmain)
    print ("Current maxcorres :", maxcorres)
    curmain += 1
    
print ("THE ANSWER IS ", maxlength, " AND THE MAXCORRES IS: ", maxcorres)