#!/usr/local/bin/python3
from string import printable
str=''
for i in range(32,127,1):
	print(chr(i),end= '  ')
	#str = str+chr(i)
print()
input('Press Enter to Continue')
len=len(str)
#for i in range(0,len,1):
#	print('{0!r}'.format(str[i]),ord(str[i]))

for i in printable:
	print('{0!r} {1:d}'.format(i),ord(i))