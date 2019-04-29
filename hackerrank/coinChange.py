def getWays(n, c):
    seek=1;count=0
    flag=True
    for i in c:

        for j in range(seek,len(c)):
            if(i+j == n):
                count+=1
            elif(i==n and flag==False):
                count+=1
                flag=False
            elif(j==n and flag==False):
                count+=1
                flag=False
            elif(i*2==n or j*2==n):
                count+=1
        seek+=1
    return count

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
