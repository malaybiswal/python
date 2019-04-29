from random import *
import datetime
a = datetime.datetime(2017,5,1,10,00,00)
b = a + datetime.timedelta(1,60) # days, seconds, then other fields.
print (a.date(),a.time())
print (b.date(),b.time())

countTime=str(b.date())+" "+str(b.time())
print(countTime,'----',randint(1, 100) )

for i in range(60,43260,60):
	countTime=str(a.date())+" "+str(a.time())
	print(countTime)
	a=a+datetime.timedelta(0,60)
	print(a)
