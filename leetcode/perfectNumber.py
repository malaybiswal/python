#https://leetcode.com/problems/perfect-number/
import math
def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    sum=1
    #num=abs(num)
    if(num<2):
        return False
    for i in range(2,int(math.sqrt(num))+1):
    #for i in range(2,num/i,1):
        if(num%i)==0:
            sum=sum+i
            sum=sum+(num/i)
            print(sum,i)
    print(sum)
    if(num==sum):
        return True
    else:
        return False

print(checkPerfectNumber(-6))
