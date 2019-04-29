def binarySearch(num,high,low,x):
    mid=int((low+high)/2)
    if(num[mid]==x):
        return mid
    elif(x<mid):
        high=mid-1
        return binarySearch(num,high,low,x)
    elif(x>mid):
        low=mid+1
        return binarySearch(num,high,low,x)
num=[2,4,6,8,10,18,21]
x=18
low=0
high=len(num)
#high=num[len1-1]
print(high)
print(binarySearch(num,high,low,x))
