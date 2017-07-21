num = 2**1000
summ = 0
for x in range(0, len(str(num))):
    summ += int(str(num)[x])
    
print (summ)