n,k=map(int,input().strip().split(' '))
numbers=[]
data=[[0 for row in range(0,3)] for col in range(0,k)]
#for i in range(0,4):
#    for j in range(0,k+1):
#        data[i][j]=0
max=0
for i in range(0,n):
    numbers.append(0)
#print(numbers)
for i in range(0,k):
    data[0][i],data[1][i],data[2][i]=map(int,input().strip().split(' '))
print("numrows:",len(data),"numcols:",len(data[0]))
for i in range(0,k):
    start=data[i][0]
    end=data[i][1]
    inc=data[i][2]
    for x in range(start,end):
        print(start,end,inc)
        print(numbers)
        numbers[x]=numbers[x]+inc
        if(max<numbers[x]):
            max=numbers[x]
print(max)
"""You are given a list of size , initialized with zeroes. You have to perform  operations on the list and output the maximum of final values of all the  elements in the list. For every operation, you are given three integers ,  and  and you have to add value  to all the elements ranging from index  to (both inclusive).

Input Format

First line will contain two integers  and  separated by a single space.
Next  lines will contain three integers ,  and  separated by a single space.
Numbers in list are numbered from  to .

Constraints






Output Format

A single line containing maximum value in the updated list.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After first update list will be 100 100 0 0 0.
After second update list will be 100 200 100 100 100.
After third update list will be 100 200 200 200 100.
So the required answer will be 200."""
