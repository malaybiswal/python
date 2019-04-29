def partition(A,low,high):
    pivot = A[low]
    pIndex=low
    for i in range(low+1,high+1):
        if(A[i]<pivot):
            pIndex=pIndex+1
            A[i],A[pIndex]=A[pIndex],A[i]
            print(A,"SWAP A[i] and A[pIndex]:",A[i],"-",A[pIndex],"-pINDEX-",pIndex,"-pivot-",pivot,"-A[i]-",A[i],"-i-",i)
        else:
            print(A,"NOTHING:",i,"-",A[i],"pINDEX:",pIndex)

            #low=low+1
    A[low],A[pIndex]=A[pIndex],A[low]
    #return pIndex
    return A

def quicksort(A,start,end):
    if(start<end):
        pIndex=partition(A,start,end)
        quicksort(A,start,pIndex-1)
        quicksort(A,pIndex+1,end)
    return A
A=[17,41,5,22,54,6,29,3,13]
#A=[1,9,4,5,6]
#A=[20,5,19,8,80,45,6]
#A=[7,8,4,5,3,2,1,9]
#A=[7,2,1,6,8,5,3,4]
#print(quicksort(A,0,len(A)-1))
print(partition(A,0,len(A)-1))
#print(quicksort(A,0,len(A)-1))
