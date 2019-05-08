#https://leetcode.com/problems/length-of-last-word/
def lengthOfLastWord(s):
    s=s.strip()
    st=s.split()
    ln=len(st)
    print("ln",ln)
    if(ln==0):
        #length=len(s.strip())
        #print("--length:",length)
        #if(length==0):
        return 0
        #else:
        #return len(s)
    else:
        length=len(st[ln-1])
        print("length:",length)
        if(length==1):
            return 1
        else:
            return length
    #return len(st[ln-1])
s=" ab  cd    efg"
print("OUTPUT:",lengthOfLastWord(s))