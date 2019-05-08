#https://leetcode.com/problems/first-unique-character-in-a-string/
def firstUniqChar(s):
    dict_s={}
    for i in s:
        if i not in dict_s:
            dict_s[i]=1
        else:
            dict_s[i]+=1
    print(dict_s)
    '''for d in dict_s:
        if(dict_s[d]==1):
            return s.index(d)'''
    for i in range(len(s)):
            if dict_s[s[i]] == 1:
                return i
    return -1
            
s = "leetcode"
print(firstUniqChar(s))
