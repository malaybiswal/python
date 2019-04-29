"""Server Updates

This program creates two sets from the contents of two files by
nesting an open within a list function which is within a set
function.  While this level of nesting is not recommended, it's
good to know it actually works.

The servers set contains a master list of servers to be updated.
The updates set contains the latest set of servers that have been
updated.  The update items are submitted manually by the admin
responsible for the server.  Sometimes, they are not accurate.
"""

# updates = set(open('c:/pydata/serverupdates.txt', 'r'))
# servers = set(open('c:/pydata/servers.txt', 'r'))
updates = set(open('/Users/mala0858/malay/python/PythonIIData/serverupdates.txt', 'r'))
servers = set(open('/Users/mala0858/malay/python/PythonIIData/servers.txt', 'r'))
str=''
str1=''
NotExitsInMatsers= servers.issubset(updates)
print('whether the list of updates exists in the master server list:',NotExitsInMatsers)

setNotExitsInMatsers=updates-servers
for j in setNotExitsInMatsers:
	str1 = str1+j
str1=str1.splitlines()
str1='\n'.join(str1)

print('Number of Servers not in Masters: {0}   List of updates exists in the master server list: {1}'.format(len(setNotExitsInMatsers),str1))

validUpdates=servers-updates
#print(validUpdates)

print(len(servers),len(validUpdates),len(updates)-len(setNotExitsInMatsers))

fo = open("/Users/mala0858/malay/python/PythonIIData/newServer.txt", "w+")
fo.seek(0,0)
for i in validUpdates:
	str=str+i
str=str.splitlines()
str = '\n'.join(str)
print(type(str))
fo.write( str )
fo.close()


