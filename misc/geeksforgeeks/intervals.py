import math
#Given a collection of Intervals,merge all the overlapping Intervals.
#https://practice.geeksforgeeks.org/problems/overlapping-intervals/0
def find(item,flag):
    for i in flag:
        print("-------->",i," COMPARES WITH:",item,"--",flag)
        if(i==item):
            print("RETURNING 1")
            return 1#found
        else:
            print("RETURNING 0")
    return 0#not found
    
k=0;x=0;y=0;start=list();end=list()
num_array=input()
num_array=list(map(int,num_array.split(' ')))
length=len(num_array)
start_length=math.ceil(length/2)
end_length=math.floor(length/2)
start=start_length*[0]
end=end_length*[0]
for i in num_array:
    #print("K:",k,"I:",i,"x:",x,"y:",y)
    if(k%2==0):
        start[x]=i
        x+=1
    else:
        end[y]=i
        y+=1
    k+=1
print("START BEFORE SORTING:",start)
print(end)

#start.sort()
#end.sort()

#print(start)
#print(end)

d={};counter=0
for i in start:
    d[i]=counter
    counter+=1
print(d)
start.sort()
print("--------START AFTER SORTING:",start)
location=0
flag=[99];newend=end_length*[0]

for i in start:
    print(d[i],"**",location,end[location],"--",flag,"XXXX")
    if(d[i]!=location and find(end[location],flag)==0):
        print("INSIDE IF")
        temp1=end[d[i]]
        temp2=end[location]
        
        newend[location]=temp1
        location+=1
        print("i:",i,"temp1:",temp1,"temp2:",temp2)
        print("----------",newend)
        flag.append(temp2)
    else:
        newend[location]=end[location]
        print("INSIDE ELSE")
        location+=1
print("------END AFTER SORTING:",newend)
        
final=[]
for i in range(0,len(start)-1):
    print("I:",i,final)
    if(i==0):
        
        if(start[i+1]<newend[i]):
            if(newend[i+1]>newend[i]):
                final.append(start[i])
                final.append(newend[i+1])
            elif(newend[i+1]<=newend[i]):
                final.append(start[i])
                final.append(newend[i])
        elif(start[i+1]>=newend[i]):
            #final.append(start[i])
            #final.append(end[i])
            final.append(start[i+1])
            final.append(newend[i+1])
    else:
        if(start[i+1]<final[1] and newend[i+1]<final[1]):
            x=0
        elif(start[i+1]>final[1] and newend[i+1]>final[1]):
            final.append(0)
            final.append(0)
            for ii in range(len(final)-1,-1,-1):
                
                if(ii==0):
                    final[ii]=start[i+1]
                    print("START I+1:",start[i+1],start)
                elif(ii==1):
                    final[ii]=newend[i+1]
                    print("END+1:",end[i+1],newend)
                else:
                    
                    final[ii]=final[ii-2]
                    print(ii,"--------",final)
        elif(start[i+1]<final[1] and newend[i+1]>final[1]):
            final[1]=newend[i+1]
            print("LAST ELIF:",final)
        
print(final)