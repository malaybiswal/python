#This is regular recursion with O(n**2) time complexity
'''def fib(n):
    if(n==1 or n==2):
        result = 1
    else:
        result=fib(n-1)+fib(n-2)
    return result
print(fib(35))'''
#This is DP with O(n) Time complexity
'''def fibDP(memo,n):
    if memo[n] is not None:
        return memo[n]
    if n==1 or n==2:
        result = 1
    else:
        result = fibDP( memo,n-1)+fibDP( memo,n-2)
    memo[n] = result
    return result
def fib_memo(n):
    memo=[None]*(n+1)
    return fibDP(memo,n)
    
    
print(fib_memo(1000))'''
#Bottom Up approach. This will not have recursion error which DP has at n=1000
def fibBottomUp(n):
    if n==1 or n==2:
        return 1
    else:
        bottomup=[None]*(n+1)
        bottomup[1]=1
        bottomup[2]=1
        for i in range(3,n+1):
            bottomup[i]=bottomup[i-1]+bottomup[i-2]
        return bottomup[n]
n=1000
print(fibBottomUp(n))



