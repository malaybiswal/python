def fibonacci(n):
    f=[]
    for i in range(0,n):
        if(i==0):
            f.append(0)
        elif(i==1):
            f.append(1)
        else:
            print(f,n-2,n-1)
            sum=f[i-2]+f[i-1]
            f.append(sum)
    print(f)
    return f[n-1]+f[n-2]
n = int(input())
print(fibonacci(n))
