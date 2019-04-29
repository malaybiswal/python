def bracket_match(bracket_string):
    closebracket=0
    openbracket=0
    count=0;flag=0
    for s in bracket_string:
        count+=1
        if(s=="("):
            openbracket+=1
        elif(s==")" and count>1):
            closebracket+=1
        elif(s==")" and count==1):
            openbracket+=1
            flag=1
        elif(s=="(" and flag==1):
            closebracket+=1
            flag=0
    return(openbracket-closebracket)
i=bracket_match(")(())(")
print(i)
