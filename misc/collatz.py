def calc(n):
    while(n>=1):
        if(n==1):
            print(n)
            return 0
        elif(n%2==0):
            print("EVEN",n)
            return 1+calc(n/2)
        else:
            print("ODD",n)
            return 1+calc(3*n+1)

print(calc(3))
