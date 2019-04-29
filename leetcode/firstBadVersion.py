
#https://leetcode.com/problems/first-bad-version/submissions/

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    l=0
    r=n-1
    while(l<=r):
        mid=int(l+(r-l)/2)
        if isBadVersion(mid)==False:
            l=mid+1
        else:
            r=mid-1
    return l
def isBadVersion(n):
    if(n>=500):
        return True
    else:
        return False

print(firstBadVersion(100))