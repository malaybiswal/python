#!/usr/local/bin/python3

count=0;
total=0;
fin = open('/Users/mala0858/malay/python/PythonIIData/alice_in_wonderland.dat','r')

x= fin.read()
count=x.count('e')+x.count('E');




for str in x:
	if(str.isalpha()):
		total=total+1
		

pct=(float)((count/total)*100)
print('Total letters: {0:,d}'.format(total))
print('Total occurrences of e or E: {0:,d}'.format(count))
#print(pct)
print('{0:.2%} of all the letter are e\'s'.format(pct/100))
fin.close()