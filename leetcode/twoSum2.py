#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
def twoSum( numbers, target):
    low=0
    high=len(numbers)-1
    while(low<high):
        res=numbers[low]+numbers[high]
        if(res==target):
            return low+1,high+1
        elif res>target:
            high-=1
        else:
            low+=1
        



n=[2,7,11,15]
t=9
print(twoSum(n,t))