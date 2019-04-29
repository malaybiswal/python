#!/usr/local/bin/python3
stack=[]
cnt=0
for i in range(0,5):
	stack.insert(i,i)
print(stack)
for j in range(len(stack)-1,-1,-1):
	x=stack.pop(j)
	print(x)
print('------------')
queue=[]
for i in range(0,5):
	queue.insert(i,i)
print(queue)
for k in range(0,5):
	y=queue.pop(k-cnt)
	cnt+=1
	print(y)



#pct=(float)((count/total)*100)
#print('Total letters: {0:,d}'.format(total))
#print(count)
#print(pct)
#print('{0:.2%} of all the letter are e\'s'.format(pct/100))