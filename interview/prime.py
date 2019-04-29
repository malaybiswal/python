
import math
n=100
i=2
sqrt = int(math.sqrt(n))
for i in range(i,sqrt):
    if(i%sqrt==0):
        print(i,"is not prime")
    else:
        print(i,"is prime")
