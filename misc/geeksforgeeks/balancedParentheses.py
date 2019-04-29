#Check for Balanced Parentheses
p=input("Input Parentheses:")
p=str(p)
print(p)
arr=[0]*50
#top=-1

def push(x,top): 
    top+=a1
    arr[top]=x
    print("TOP",top,"arr[top]:",arr[top])
    
    return top

def pop(top):
    if(top==-1):
        print("ERROR: No ELEMENT TO POP")
        return -1
    top-=1
    return top

def ismatchingPair(openingChar,closingChar):
    if((openingChar=='(') and (closingChar==')')):
        print("1st",openingChar,"-",closingChar)
        return True
    elif((openingChar=='{') and (closingChar=='}')):
        print("2nd",openingChar,"-",closingChar)
        return True
    elif((openingChar=='[') and (closingChar==']')):
        print("3rd",openingChar,"-",closingChar)
        return True
    else:
        print("NONE",openingChar,"-",closingChar)
        return False

top=-1             
for char in p:
    
    if((char=='(') or (char=='{') or (char=='[')):
        top=push(char,top)
    elif((char==')') or (char=='}') or (char==']')):
        if(ismatchingPair(arr[top],char)):
            top=pop(top)
if(top==-1):
    print("MATCHING",top)
else:
    print("NOT MATCHING",top)
           

        
