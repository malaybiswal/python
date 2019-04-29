#Find index of minimum element of sorted array with no duplicate
def findRotation(arr,n):
    low=0
    high=n-1
    while(low<=high):
        mid=int(low+(high-low)/2)
        next=(mid+1)%n
        previous=(mid+n-1)%n
        if(arr[low]<=arr[high]):
            return low
        elif(arr[mid]<=arr[next] and arr[mid]<=arr[previous]):
            return  mid
        elif(A[mid]<=A[high]):
            high=mid-1
        elif(A[mid]>=A[low]):
            low=mid+1
        else:# This is for cases such as array with everything rotataed like 9,8,7,6
            low=mid+1
    return -1
#A=[9,8,7,6,5,4]
#A=[11,12,15,18,2,5,6,8]
#A=[1,2,3,4,5,6]
A=[15,22,23,28,31,38,78,5,6,8,10,12]
n=len(A)
print("Rotated ",findRotation(A,n)," Times")
