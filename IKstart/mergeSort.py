def mergeSort(list):
	if len(list) < 2:
		return list

	middle = int(len(list)/2)
	left = mergeSort(list[:middle])
	right = mergeSort(list[middle:])

	return merge(left, right)

def merge(L,R):
    i=0;j=0;k=0
    nL=len(L);nR=len(R)
    A=(nL+nR)*[0]
    #print("FROM merge A is:",A)
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
    print("FROM merge A is:",A)
    return A

#L=[1,4,7,9]
#R=[3,5,8]
#A=[]
#print(merge(L,R,A))

A=[1,90,12,45,34,11,7]
print("After sorting:",mergeSort(A))
