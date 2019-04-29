# This merge 2 sorted arrays, which is required in merge sorted
def merge(L,R):
    i=0;j=0;k=0
    nL=len(L);nR=len(R)
    A=(nL+nR)*[0]
    print(A)
    while(i<nL and j<nR):
        if(L[i]<R[j]):
            A[k]=L[i]
            i+=1
        elif(R[j]<L[i]):
            A[k]=R[j]
            j+=1
        k+=1
    while(i<nL):
        A[k]=L[i]
        k+=1
        i+=1
    while(j<nR):
        A[k]=R[j]
        k+=1
        j+=1
    return A

L=[1,4,7,9]
R=[3,5,8]
A=[]
print(merge(L,R))
