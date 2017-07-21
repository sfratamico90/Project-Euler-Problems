summ = 0
for x in range(1,1000):
    summ += (x**x)
    summ = sum%(100000**2)
print (summ)