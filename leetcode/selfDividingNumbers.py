#https://leetcode.com/problems/self-dividing-numbers/
#NOT DON> NEED TO FIX THIS
def selfDividingNumbers(left,right):
    l=[]
    flag=False
    for i in range(left,right,1):
        x=[int(j) for j in str(i)]
        for k in range(0,len(x)-1):
            if(i%x[k]==0):
                flag=True
                continue
            else:
                flag=False
                break
        if(flag==True):
            l.append(i)
    return l
        

print(selfDividingNumbers(1,22))