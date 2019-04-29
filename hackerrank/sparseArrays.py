num1=int(input().strip())
s={};query=[]
for i in range(0,num1):
    string=str(input().strip())
    try:

            s[string]=s[string]+1
    except:
        s[string]=1

num2=int(input().strip())
for i in range(0,num2):
    query.append(input().strip())
#print("----------------")
#print(s)
#print(query)
for q in query:
    try:
        print(s[q])
    except:
        print(0)

"""There are  strings. Each string's length is no more than  characters. There are also  queries. For each query, you are given a string, and you need to find out how many times this string occurred previously.

Input Format

The first line contains , the number of strings.
The next  lines each contain a string.
The nd line contains , the number of queries.
The following  lines each contain a query string.

Constraints





Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab
Sample Output

2
1
0
Explanation

Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string, and "ab" does not occur at all."""
