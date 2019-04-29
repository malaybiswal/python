#https://leetcode.com/problems/contains-duplicate/
def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    l1=len(nums)
    l2=len(set(nums))
    if(l1!=l2):
        return True
    else:
        return False
arr=[1,2,3,4,6,2]
print(containsDuplicate(arr))