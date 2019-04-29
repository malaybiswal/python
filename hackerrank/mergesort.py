def mergesort(l):
    left=[]
    right=[]
    n=len(l)
    if(n<2):
        return l
    else:
        mid=int(n/2)
        #left=[0]*mid
        #right=[0]*(n-mid)
        for i in range(0,mid):
            left.append(l[i])
        #    left[i]=l[i]
        for i in range(mid,n):
            right.append(l[i])
        #    right[i-mid]=l[i]
        print("-----",left,right)
        mergesort(left)
        mergesort(right)
        merge(left,right,l)
def merge(left,right,l):

    nl=len(left)
    nr=len(right)
    #l=[0]*(nl+nr)
    print("*********L:",l)
    i=0;j=0;k=0
    while(i<nl and j<nr):
        print(i,j,k,"---",left[i],right[j]," *** ",l)
        if(left[i]<right[j]):
            l[k]=left[i]
            i+=1
        else:
            l[k]=right[j]
            j+=1
        k=k+1
    while(i<nl):
        l[k]=left[i]
        i=i+1
        k=k+1
    while(j<nr):
        l[k]=right[j]
        j=j+1
        k=k+1
    #return l

l=[100,1,2,3,45,4,7,6,90,45]
#l1=[1,4,8]
#l2=[2,5,6,9]
#l=merge(l1,l2)
mergesort(l)
print(l)
