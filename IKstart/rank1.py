def magic(data,start,end):
    pivot=data[0]
    #start=1
    #end=len(data)-1
    i=0
    while(start<=end):
        i+=1
        if((pivot<data[start]) and (start<end)):
            temp=data[start]
            data[start]=data[end]
            data[end]=temp
            end=end-1
            print(start,end,"#")
        elif((pivot>data[start]) and (start==end)):
            temp=data[0]
            data[0]=data[start]
            data[start]=temp
            start=start+1
            print("start end same")

        else:
             start=start+1
        print(data,"data after",i," times ",data[start]," ",data[end])
    if(start>end):
        if(pivot>data[end]):

            temp=pivot
            data[0]=data[start]
            data[start]=temp
    print("ater 1st pass:",data)
    return start

#data=[1,9,4,6,5]
#data=[7,8,4,5,3,2,1,9]
data=[20,5,19,8,80,45,6]
start=1
end=len(data)-1

print("Before starting data:",data)
print(magic(data,start,end))
