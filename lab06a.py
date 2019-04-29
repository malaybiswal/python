#!/usr/local/bin/python3

count=0;
cnt=0
total=0;
fin = open('/Users/mala0858/malay/python/PythonIIData/alice_in_wonderland.dat','r')

x= fin.read()
x=x.upper()
#count=x.count('e')+x.count('E');

d=dict()


for str in x:
	if(str.isalpha()):
		if str not in d:
			d[str] = 1
		else:
			d[str]+=1
print(d)
print('--------------------------')
x=sorted(zip(d.values(),d.keys()))
print(x)
#y=sorted(x)
#z=reversed(y)
#z=reversed(x)
#print(list(z))
#print(type(z))
print('**************************')

for i in reversed(x):
	#print('MALAY',i)
	cnt+=1
	if(cnt<=30):
		print(i)
	else:
		#print('IN ELSE BREAKING...',cnt)
		break		

#pct=(float)((count/total)*100)
#print('Total letters: {0:,d}'.format(total))
#print('Total occurrences of e or E: {0:,d}'.format(count))
#print(pct)
#print('{0:.2%} of all the letter are e\'s'.format(pct/100))
fin.close()