#binary SEarch with recursion
def binarySearch(arr,low,high,x):
    if(low>high):
        return -1
    mid=int(low+(high-low)/2)
    if(arr[mid]==x):
        return mid
    elif(x>arr[mid]):
        return binarySearch(arr,mid+1,high,x)
    else:
        return binarySearch(arr,low,mid-1,x)

A=[1,3,5,7,8,13,21,70,80,100]
print(binarySearch(A,0,len(A)-1,100))
