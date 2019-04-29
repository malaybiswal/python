#!/usr/local/bin/python3


fin = open('/Users/mala0858/malay/python/PythonIIData/alice_in_wonderland.dat','r')
loc=0
x= fin.read()
x=x.lower()
count=x.count("caterpillar")
count1=x.count("gryphon")
#for str in x:
loc=x.find("caterpillar")
loc1=x.find("gryphon")
locend=x.rfind("caterpillar")
locend1=x.rfind("gryphon")
print(loc,locend,count)
print(loc1,locend1,count1)

#pct=(float)((count/total)*100)
#print('Total letters: {0:,d}'.format(total))
#print(count)
#print(pct)
#print('{0:.2%} of all the letter are e\'s'.format(pct/100))