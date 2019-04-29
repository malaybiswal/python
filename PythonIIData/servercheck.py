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

NotExitsInMatsers= servers.issubset(updates)
print('whether the list of updates exists in the master server list:',NotExitsInMatsers)

setNotExitsInMatsers=updates-servers
print('Number of Servers not in Masters: {0}   List of updates exists in the master server list: {1}'.format(len(setNotExitsInMatsers),setNotExitsInMatsers))

validUpdates=servers-updates
#print(validUpdates)

print(len(servers),len(validUpdates),len(updates)-len(setNotExitsInMatsers))

fo = open("/Users/mala0858/malay/python/PythonIIData/newServer.txt", "w+")
fo.seek(0,0)
fo.writelines( validUpdates )
fo.close()


