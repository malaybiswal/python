#!/usr/local/bin/python3

count=0;
total=0;
fin = open('/Users/mala0858/malay/python/PythonIIData/alice_in_wonderland.dat','r')

x= fin.read()

for str in x:
	if((ord(str)>=65 and ord(str)<=90) or (ord(str)>=97 and ord(str)<=122)):
		total=total+1
		if((str=='e') or (str=='E')):
			count=count+1;

pct=(float)((count/total)*100)
print('Total letters: {0:,d}'.format(total))
print(count)
print(pct)
print('{0:.2%} of all the letter are e\'s'.format(pct/100))