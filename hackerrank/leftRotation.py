numElement,numLeft = map(int, input().strip().split(' '))
nums=list(map(int, input().strip().split(' ')))
#print(nums)
for i in range(1,numLeft+1):
    #x=nums[0]
    #del nums[0]
    #nums.insert(len(nums),x)
    nums.append(nums.pop(0))

    #print(nums,i,x)
for i in nums:
    print(i,end=" ")
"""A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if left rotations are performed on array , then the array would become .

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of  (the number of integers) and  (the number of left rotations you must perform).
The second line contains  space-separated integers describing the respective elements of the array's initial state.

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:

Thus, we print the array's final state as a single line of space-separated values, which is 5 1 2 3 4."""
