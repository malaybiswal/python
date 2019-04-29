#QuickSort
def quicksort(A,start,end):
    if(start<end):
        pIndex = partition(A,start,end)
        quicksort(A,start,pIndex-1)
        quicksort(A,pIndex+1,end)
    return A

def partition(A,start,end):
    pIndex=start
    pivot=A[end]
    for i in range(start,end):
        if(A[i]<pivot):
            #swap(A[i],A[PIndex])
            A[i],A[pIndex] = A[pIndex],A[i]
            pIndex=pIndex+1
    #swap(A[pIndex],pivot)
    A[pIndex],A[end] = A[end],A[pIndex]
    return pIndex
def swap(A1,A2):
    temp=A2
    A2=A1
    A1=temp

A=[30,15,20,25,5,1]
quicksort(A,0,len(A)-1)
for i in range(len(A)):
    print ("%d" %A[i]),
