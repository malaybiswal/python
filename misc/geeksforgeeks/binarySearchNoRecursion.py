#THis is binary search without recursion
def binarySearch(arr,n,x):
    start=0
    end=n-1

    while(start<=end):
        mid=int(start+(end-start)/2)
        if(x==arr[mid]):
            return mid
        elif(x>arr[mid]):
            start=start+1
        else:
            end=end-1
    return -1

A=[2,4,5,8,9,11,13,17,21]
n=len(A)
x=21
print(x,"FOUND AT LOCATION",binarySearch(A,n,x))
