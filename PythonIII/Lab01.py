dict={}
with open('/Users/mala0858/malay/python/PythonIII/Python_III/words.txt','r') as file:
    for word in file.read().splitlines():
        #entry=entry[0:-1]
        dict[word]=0

print(dict,len(dict))

with open('/Users/mala0858/malay/python/PythonIII/Python_III/alice_in_wonderland.dat','r') as fileAlice:
    dataAlice = fileAlice.readlines();
