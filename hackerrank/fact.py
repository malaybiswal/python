def factorial(n):
    while(n>0):
        if(n==1):
            return 1
        else:
            return n*factorial(n-1)

n=int(input())
res=factorial(n)
print(res)
