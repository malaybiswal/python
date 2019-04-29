def bsearch(arr,l,r,x):
    if(l<=r):
        mid=int(l+(r-l)/2)
        #mid=int((l+r)/2)
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
            return bsearch(arr,l,mid-1,x)
        else:
            return bsearch(arr,mid+1,r,x)
    else:
        return -1

arr=[4,7,10,13,20,100]
x=100
res=bsearch(arr,0,len(arr)-1,x)
if(res!=-1):
    print("Index of ",x," is:", res)
else:
    print("Element not present in array")