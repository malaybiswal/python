#https://leetcode.com/problems/valid-parentheses/
class Solution():
    def isValid(self,str):
        dict={")":"(","]":"[","}":"{"}
        res=[]
        if(len(str)%2!=0):
            return False
        for i in str:
            if (i in dict.values()):
                res.append(i)
            elif(i in dict.keys()):
                if(len(res)==0):
                    return False
                print(dict.get(i))
                if dict.get(i) == res[len(res)-1]:
                    res.pop()
            else:
                return False
        return res==[]





s = Solution()
str="(}"
print(s.isValid(str))

