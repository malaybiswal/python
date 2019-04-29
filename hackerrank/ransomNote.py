def ransom_note(magazine, ransom):
    mag=dict()
    ran=dict()
    for m in magazine:
        if(len(mag)==0):
            mag[m]=1
        else:
            count=mag.get(m)
            if(count!=None):
                count+=1
                mag[m]=count
            else:
                mag[m]=1
    for r in ransom:
        if(len(ran)==0):
            ran[r]=1
        else:
            count=ran.get(r)
            if(count!=None):
                count+=1
                ran[r]=count
            else:
                ran[r]=1
    print(ran)
    print(mag)
    for r in ran:
        i=0
        for m in mag:
            i+=1
            #print(i,r,m)
            if(r==m):
                if (ran[r]>mag[m]):
                    #print(r,m,"----same")
                    return False
                else:
                    break
            else:
                if(i==len(mag)):
                    #print(r,m,i,len(mag),"----Not Same")
                    return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

"""A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Input Format

The first line contains two space-separated integers describing the respective values of  (the number of words in the magazine) and  (the number of words in the ransom note).
The second line contains  space-separated strings denoting the words present in the magazine.
The third line contains  space-separated strings denoting the words present in the ransom note.

Constraints

.
Each word consists of English alphabetic letters (i.e.,  to  and  to ).
The words in the note and magazine are case-sensitive.
Output Format

Print Yes if he can use the magazine to create an untraceable replica of his ransom note; otherwise, print No.

Sample Input

6 4
give me one grand today night
give one grand today
Sample Output

Yes
Explanation

All four words needed to write an untraceable replica of the ransom note are present in the magazine, so we print Yes as our answer."""
