#Find Element in Circularly rotated Array
def find(arr,n,x):
    low=0
    high=n-1
    while(low<=high):
        mid=int(low+(high-low)/2)
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>=arr[low]):#Left half sorted
            if(x>=arr[low] and x<=arr[mid]):
                high=mid-1#Search in left half
            else:
                low=mid+1
        elif(arr[mid]<=arr[high]):#right half sorted
            if(x>=arr[mid] and x<=arr[high]):
                low=mid+1#search in right 2nd hlaf
            else:
                high=mid-1
    return -1

A=[12,14,18,21,3,6,8,9]
n=len(A)
x=12
print(find(A,n,x))

