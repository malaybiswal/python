def is_matched(expression):
    stack = []
    dicty = {'(':')', '[':']', '{':'}'}
    for x in expression:
        if dicty.get(x):
            stack.append(dicty[x])
            print("IN IF:",stack,x)
        else:
            print("IN ELSE:",stack,x,len(stack)-1)
            if len(stack) == 0 or x != stack[len(stack)-1]:
                print("INSIDE ELSE IF:X",x," stack[len(stack)-1]",stack[len(stack)-1])
                return False
            stack.pop()
    return len(stack) == 0
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
