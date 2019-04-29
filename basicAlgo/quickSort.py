def quickSort(arr,start,end):
    if(start<end):
        
        index=partition(arr,start,end)
        quickSort(arr,start,index-1)
        quickSort(arr,index+1,end)
    return arr
def partition(arr,start,end):
    pIndex=start
    pivot=arr[start]
    for i in range(start+1,end+1):
        if(arr[i]<pivot):
            pIndex=pIndex+1
            arr[i],arr[pIndex]=arr[pIndex],arr[i]
    arr[start],arr[pIndex]=arr[pIndex],arr[start]
    return pIndex

arr=[100,20,10,90,30,50]
print(quickSort(arr,0,len(arr)-1))

