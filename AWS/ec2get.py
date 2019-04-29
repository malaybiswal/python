from pprint import pprint
from boto import ec2
file="/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/rootkey.csv"
with open(file,'r', encoding='utf-8') as infile:
    for line in infile:
        if line.find("AWSAccessKeyId") != -1:
            lines=line.split("=")
            id=lines[1].strip()
        elif line.find("AWSSecretKey") != -1:
            lines=line.split("=")
            key=lines[1].strip()
print(id,"-",key,"-")

ec2conn = ec2.connection.EC2Connection(id, key)
reservations = ec2conn.get_all_instances()
print("RESERVATIONS:",reservations,len(reservations))
reservation = ec2conn.get_all_instances()[0]
# Yeah I don't know why they have these stupid reservation objects either...
instance = reservation.instances[0]
print (instance.tags)
print (instance.region)
print (instance._state)
print (instance.key_name)
print (instance.instance_type)
print (instance.launch_time)
print("-------------------------")
for r in reservations:
    size=len(r.instances)
    for i in range(0,size):
        print(r.instances[i].__dict__)
#instances = [i for r in reservations for i in r.instances]
#for i in instances:
#    print(i.__dict__)
#    break # remove this to list all instances
