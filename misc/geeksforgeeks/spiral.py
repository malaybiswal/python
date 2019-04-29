#Print 2D array in spiral order
w, h = 4, 4;
A = [[0 for x in range(w)] for y in range(h)] 
print(A)
A[0][0]=2
A[0][1]=4
A[0][2]=6
A[0][3]=8
A[1][0]=5
A[1][1]=9
A[1][2]=12
A[1][3]=16
A[2][0]=2
A[2][1]=11
A[2][2]=5
A[2][3]=9
A[3][0]=3
A[3][1]=2
A[3][2]=1
A[3][3]=8

T=0;B=3;L=0;R=3;dir=0
while(T<=B and L<=R):
    if(dir==0):
        for i in range(L,R+1):
            print(A[T][i])
        T+=1
        dir=1
    elif(dir==1):
        for i in range(T,B+1):
            #print("i:",i," R:",R)
            print(A[i][R])
        R-=1
        dir=2
    elif(dir==2):
        for i in range(R,L-1,-1):
            #print("--B:",B," i:",i)
            print(A[B][i])
        B-=1
        dir=3
    elif(dir==3):
        for i in range(B,T-1,-1):
            #print("**i:",i," L:",L)
            print(A[i][L])
        L+=1
        dir=0
    
        
        
