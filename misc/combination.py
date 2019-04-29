#choose 4 people as a group out of 60 people answer will be 60!/(4!*(60-4)!) which is 487635.
#This is combination C(n,k) which is n!/(k!*(n-k)!)
def C( n,  k):
    if(k==0 or k==n):
        return 1
    else:
        return C(n-1,k)+C(n-1,k-1)
print(C(60,4))
