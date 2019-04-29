#Find missing numbers from array
class missNum:
    def __init__(self):
        print("INSIDE init:")
def missNum(l,arr):
    count=1
    l=int(l)
    a=int(arr[0])
    flag=True
    for i in arr:
        i=int(i)
        #print(i," ",count)
        if(i==count):
            count=count+1
            continue
        else:
            return count
        #count=count+1
        #print("COUNT:",count)
    if(flag):
        return(count)

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


#print("Enter length of array:")
ip = input()
ip=int(ip)
for i in range(1,ip+1):

    length = input()
    #print("Enter array:")
    #arr = [i for i in input().split(",")]
    try:
        input_list = input().split(' ')
        arr = [int(x.strip()) for x in input_list]
        quicksort(arr,0,len(arr)-1)
        #print(arr)
        #sorted(arr)
        #print("ARRAY LENGTH:",len(arr))
        num=missNum(length,arr)
        print(num)
    except:
        print(0)

    #print(arr)
