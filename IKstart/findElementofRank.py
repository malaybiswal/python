def findElement(data,k):
    m=magic(data)
    #m=m-1
    #index=data.index(data[m-1])
    while(len(data)>0):
        index=data.index(data[m-1])
        if(m<k):
            data=data[:index]
            magic(data)
        else:
            data=data[index:len(data)]
            magic(data)
    return data[m]



def magic(data):
    pivot=data[0]
    start=1
    end=len(data)-1
    while(start<end):
        if(pivot<data[start]):
            temp=data[start]
            data[start]=data[end]
            data[end]=temp
            end=end-1

        else:
             start=start+1
    return start

data=[20,5,19,8,80,45,6]
print(findElement(data,3))
