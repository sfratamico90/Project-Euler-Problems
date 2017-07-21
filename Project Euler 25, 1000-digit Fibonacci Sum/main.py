FibIndex = []

def catch(n):
    if(len(str(n))<1000):
        return False
    else:
        return True
fib_a = [1,1]
fib_b = [2,1]
cur_i = 2;
fib_cur = [0,0]
FibIndex = [fib_a, fib_b]

while (catch(fib_cur[1])== False):
    fib_cur = [cur_i + 1, fib_a[1] + fib_b[1]]
    cur_i += 1
    fib_a = fib_b
    fib_b = fib_cur
    FibIndex.append(fib_cur)
    print ("cur is: ", cur_i, " and fib_cur is: ", fib_cur)