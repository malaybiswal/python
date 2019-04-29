def firstOccurence(arr,l,r,num):
    res=-1
    while(l<=r):
        mid=int((l+r)/2)
        #res=-1
        if(arr[mid]==num):
            #return mid
            res=mid
            r=mid-1
        elif(arr[mid]>num):
            r=mid-1
        else:
            l=mid+1
    return res
    #return -1

a=[6,6,6,6,14,15,60,60]
x=60
print(firstOccurence(a,0,len(a)-1,x))
