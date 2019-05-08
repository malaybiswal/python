#https://leetcode.com/problems/min-stack/
# Need 2 stacks. minStack to track minimum elment so minimum element can be searched by O(1)
class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self,x):
        self.stack.append(x)
        if(len(self.minStack)==0):#1st element append to miStack too
            self.minStack.append(x)
        else:
            topMinElement=self.minStack[-1]
            if x<=topMinElement: #If elementgettuing pushed is less than minstack top element then push to MinStack
                self.minStack.append(x)
            

        print("APPENDING:",self.stack,self.minStack)

    def pop(self):
        if(self.stack[-1]==self.minStack[-1]): # If both stacks top elemnts matching pop from minStack as well
            self.minStack.pop()
            self.stack.pop()
        else:
            self.stack.pop()
        print("POP:",self.stack,self.minStack)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

l=[]
minStack =  MinStack()

minStack.push(7)
minStack.push(9)
minStack.push(5)
minStack.push(3)
minStack.push(5)
minStack.push(10)
print("TOP:",minStack.top())
print("MIN:",minStack.getMin())
minStack.pop()
minStack.pop()
minStack.pop()
print("TOP:",minStack.top())
print("MIN:",minStack.getMin())

