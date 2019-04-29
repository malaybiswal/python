#https://leetcode.com/problems/valid-perfect-square/
def perfectsuare(x):
    mid=int(x/2)
    flag=False
    if(x==0):
        return 0
    else:
        while(True):
            if(mid*mid>x):
                if(flag==True):
                    return False
                mid=int(mid/2)
            elif(mid*mid<x):
                mid=mid+1
                flag=True
                
            else:
                return True
        return False
print(perfectsuare(225))
