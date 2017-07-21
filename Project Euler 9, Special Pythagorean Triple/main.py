a = 0
b = 0
for x in range(1,999):
    for y in range (1, 999):
        if (x + y + float((x**2 + y**2)**(.5)) == 1000):
            a=x 
            b=y
        
print ((a*b)*((a**2 + b**2)**(.5)))