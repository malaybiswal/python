def quicksort(data,start,end):
    if(start<end):
        index = partition(data,start,end)
        quicksort(data,start,index-1)
        quicksort(data,index+1,end)
    return data

def partition(data,start,end):
    pIndex=start
    pivot=data[start]
    for i in range(start+1,end+1):
        if(data[i]<pivot):
            pIndex=pIndex+1
            data[i],data[pIndex]=data[pIndex],data[i]

    data[start],data[pIndex]=data[pIndex],data[start]
    return pIndex
data=[7,8,4,5,3,2,1,9]

print(quicksort(data,0,len(data)-1))
