#https://leetcode.com/problems/degree-of-an-array/
def findShortestSubArray(nums):
    dict={}
    for i in range(0,len(nums)):
        element=nums[i]
        if element not in dict:
            dict[element]=[1,i,i]
        else:
            dict[element][0]+=1
            dict[element][2]=i
    maxDegree=0
    for val in dict.values():
        if (val[0]>maxDegree):
            maxDegree=val[0]
    
    minDiff=len(nums)
    for key,val in dict.items():
        if val[0]==maxDegree:
            diff=(val[2]-val[1])+1
            if(diff<minDiff):
                minDiff=diff
    return minDiff 
    


nums=[1,2,2,3,1,4,2]
print(findShortestSubArray(nums))