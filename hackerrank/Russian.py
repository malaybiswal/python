n,k=map(int,input().strip().split(' '))
numbers=[]
l1=[];l=[]
max=0
for i in range(0,n):
    numbers.append(0)
#print(numbers)
for i in range(0,k):
    l1=list(map(int,input().strip().split(' ')))
    l.append(l1)
#print(l)
for i in l:
    #print(i[0])
    #print(i[1])
    #print(i[2])
    start= i[0]
    end=i[1]
    inc=i[2]
    for j in range(start,end):
        #print(start,end)
        numbers[j]=numbers[j]+inc
        if(numbers[j]>max):
            max=numbers[j]
        else:
            max=max
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
