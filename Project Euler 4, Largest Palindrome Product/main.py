highestPali = 0
def isPali(n):
    if(len(str(n)) == 5):
        if (str(n)[0] == str(n)[4] and str(n)[1] == str(n)[3]):
            return True
        else:
            return False
    else:
        if (str(n)[0] == str(n)[5] and str(n)[1] == str(n)[4] and str(n)[2] == str(n)[3]):
            return True
        else:
            return False


for x in range (100, 999):
    for y in range (100, 999):
        highestPali = (x*y if isPali(x*y) and x*y > highestPali else highestPali)
print (highestPali)