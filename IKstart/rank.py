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
            print(start,end,"#")
        
        else:
             start=start+1
    temp=pivot
    data[0]=data[start]
    data[start]=temp
    print("ater 1st pass:",data)
    return start

data=[7,8,4,5,3,2,1,9]
#data=[20,5,19,8,80,45,6]
print("Before starting data:",data)
print(magic(data))
