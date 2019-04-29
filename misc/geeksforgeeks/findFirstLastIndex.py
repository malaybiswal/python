#This find first occurrence and last occurrence of elements in a sorted Array
def find(arr,n,x,flag):
    low=0
    high=n-1
    result=-1
    while(low<=high):
        mid=int(low+(high-low)/2)
        if(arr[mid]==x):
            result=mid
            if(flag):
                high=mid-1
            else:
                low=mid+1
        elif(x>arr[mid]):
            low=mid+1
        else:
            high=mid-1
    return result

A=[1,1,1,2,3,5,10,10,10,10,20,24,30]
element=300
firstIndex=find(A,len(A),element,True)
if(firstIndex==-1):
    print("COUNT OF ",element," IS ",0)

else:
    lastIndex=find(A,len(A),element,False)
    print("FIRST occurrence:",firstIndex,"Last Occurrence:",lastIndex)
    print("COUNT IS",lastIndex-firstIndex+1," Times")
