#https://leetcode.com/problems/sqrtx/
def sqrt(x):
    mid=int(x/2)
    flag=False
    if(x==0):
        return 0
    else:
        while(True):
            if(mid*mid>x):
                
                if(flag==True):
                    return mid-1
                mid=int(mid/2)
            elif(mid*mid<x):
                mid=mid+1
                flag=True
            else:
                return mid
print(sqrt(227))
