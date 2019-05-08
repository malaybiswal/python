#https://leetcode.com/problems/pascals-triangle-ii/
def getRow(rowIndex):
    d={}
    d[0]=[1]
    d[1]=[1,1]
    l=[]
    p=[]
    for i in range(2,rowIndex+1):
        #print(i)
        print("D:",d,"I:",i)
        l=d[i-1]
        print(d,i,l,"LENGTH OF L:",len(l))
        #p.append(1)
        for j in range(0,len(l)):
            print("J:",j,"LENGTH OF L:",len(l)-1)
            if(j==0):
                p.append(1)
            elif(j!=(len(l)-1)):
                
                temp=l[j]+l[j-1]
                p.append(temp)
                #temp=l[j]+l[j+1]
                #p.append(temp)
                


                print("P:",p,"J:",j)
            elif(len(l)==2):
                temp=l[0]+l[1]
                p.append(temp)
                p.append(1)
                d[2]=p
                print("INSIDE 2nd ELIF P:",p,"J:",j)
                print("INSIDE 2ndELIF****",d[j])
                p=[]
            elif(j==len(l)-1):
                p.append(l[j-1]+l[j])
                p.append(1)
                d[i]=p
                print("INSIDE ELIF****",d[j],d)
                p=[]
        print("P:",p)
    return d[rowIndex]

print(getRow(3))

