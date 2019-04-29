#Find Excel column name from a given column number
#https://www.geeksforgeeks.org/find-excel-column-name-given-number/
def get(num):
    string = ["\0"]*50
    i=0
    while(num>0):
        rem = num%26
        if(rem==0):
            string[i]='Z'
            i+=1
            num=int(num/26)-1
        else:
            print("----",rem)
            string[i]=chr((rem-1)+ord('A'))
            #string[i]=chr(rem)
            i+=1
            num=int(num/26)
    #string[i]='\0'
    string=string[::-1]
    print("".join(string))
    #print(string)
    
get(705)
