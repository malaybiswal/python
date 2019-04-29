def qs(A):
   quicksort(A,0,len(A)-1)
   #return A
def quicksort(A,start,end):
    if(start>=end):
        return A
    else:
        pIndex=partition(A,start,end)
        quicksort(A,start,pIndex-1)
        quicksort(A,pIndex+1,end)
    #return A
def partition(A,start,end):
    pivot=A[end]
    pIndex=start
    print(pIndex,pivot)
    for i in range(start,end-1):
        if(A[i]<=pivot):
            temp=A[i]
            A[i]=A[pIndex]
            A[pIndex]=temp
            pIndex+=1
    temp=A[pIndex]
    A[pIndex]=A[end]
    A[end]=temp
    print("pIndex",pIndex)
    print(A)
    return pIndex
A=[7,5,4,2,10,6]
#for i in range(0,5):
#    A[i]=int(input().strip())
print(A)
qs(A)
print(A)
