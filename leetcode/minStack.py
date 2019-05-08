#https://leetcode.com/problems/min-stack/
class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self,x):
        self.stack.append(x)
        if(len(self.minStack)==0):
            self.minStack.append(x)
        else:
            topMinElement=self.minStack[-1]
            if x<=topMinElement:
                self.minStack.append(x)
            

        print("APPENDING:",self.stack,self.minStack)

    def pop(self):
        if(self.stack[-1]==self.minStack[-1]):
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

