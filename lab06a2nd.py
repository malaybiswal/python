#!/usr/local/bin/python3

count=0;
cnt=0
total=0;
fin = open('/Users/mala0858/malay/python/PythonIIData/alice_in_wonderland.dat','r')

x= fin.readlines()
#count=x.count('e')+x.count('E');

d=dict()


for str in x:
	count+=1
	print('**',str)
	if(str.isalpha()):
		print('##',str)
		if str not in d:
			d[str] = 1
		else:
			d[str]+=1
	print(d)
	print('--------------------------')
	x=sorted(zip(d.values(),d.keys()))
	print(x)
	print('**************************')

	for i in reversed(x):
	#print('MALAY',i)
		cnt+=1
		if(cnt<=5):
			print(i)
		else:
			#print('IN ELSE BREAKING...',cnt)
			cnt=0
			break
	if(count==6):
		break	

print(count)
fin.close()