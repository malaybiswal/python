#STACK
arr=[0]*5
top=-1
def push(x,top):
    top+=1
    arr[top]=x
    return top

def pop(top):
    if(top==-1):
        print("ERROR: No ELEMENT TO POP")
        return -1
    top-=1
    return top
def display():
    for i in range(0,top+1):
        print(arr[i])
    print("----------")
def isEmpty(top):
    if(top==-1):
        print("EMPTY")
    else:
        print("NOT EMPTY")

top=push(1,top)
top=push(5,top)
#print(top)
display()
top=pop(top)
display()
isEmpty(top)
top=pop(top)
display()
isEmpty(top)
top=pop(top)