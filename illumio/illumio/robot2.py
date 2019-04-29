def left(direction):
    """Turning left"""
    #print("BEFORE LEFT MOVE:",direction)
    ind=dir.index(direction)
    if(ind==0):
        direction="S"
    else:
        direction=dir[ind-1]
    #print("DIRECTION AFTER MOVIING LEFT:",direction)
    return direction

def right(direction):
    """Turning right"""
    #print("BEFORE RIGHT MOVE:",direction)
    ind=dir.index(direction)
    #print("INDEX:",ind)
    if(ind==3):
        direction="W"
    else:
        direction=dir[ind+1]
    #print("DIRECTION AFTER MOVIING RIGHT:",direction)
    return direction
def move(x,y,direction):
    """Moving """
    #print("BEFORE MOVING CO_ORDINATE:",x,y,direction)
    x=int(x);y=int(y);direction=direction.strip()
    if(direction=="N"):
        y=y+1
        #print("IN IF N: y is:",y)
    elif(direction=="S"):
        y=y-1
        #print("IN IF S: y is:",y)
    elif(direction=="E"):
        x=x+1
        #print("IN IF E: x is:",x)
    elif(direction=="W"):
        x=x-1
        #print("IN IF W: x is:",x)
    z=str(x)+" "+str(y)+" "+direction
    #print("AFTER MOVE:",z)
    return z
fname="robot.txt"
line=0
side=[]
dir=["W","N","E","S"]
with open(fname) as f:
    content=f.readlines()
    content = [x.strip() for x in content]
    #print("conetnet",content)
    xmax,ymax=map(int,content[0].strip().split(' ') )
    length=len(content)
    #print(length)
    for i in range(1,length):
        side=[]
        #print("INSIDE LOOP:",i," ",content[i])
        if(i%2!=0):
            x,y,direction=map(str,content[i].strip().split(' '))
            x=int(x);y=int(y)
            print("Initial coordinates:",content[i])
        else:
            print("After ",content[i]," moves")
            for j in content[i]:
                side.append(j)

            for s in side:
                if(s=="L"):
                    direction=left(direction)
                elif(s=="R"):
                    direction=right(direction)
                elif(s=="M"):
                    x,y,direction=map(str,move(x,y,direction).split(' '))
            print("FINAL CO_ORDINATE",x,y,direction)
            print("----------------------------")
        #print("-----------------------------------------")

#print(xmax,ymax)
#print(side)

"""You are given a few Lego Mindstorm-like robots and asked to navigate a rectangular plateau, so that the on-board cameras will get a complete view of the terrain. The robots are expensive and should not get damaged in any way.

The robot's position and location is a combination of (X,Y) coordinates and a letter representing four cardinal compass points.
The field is divided into a grid. For example, the bottom left of the field is (0,0,N) with the robot pointing North. The square directly North of the current point of (X,Y) is (X, Y+1).

Commands you can send the robot:
L, R - spin 90 degrees left or right
M - move forward one point and maintain the same heading

You will be given input in text format. The first line is always two numbers indicating the top right coordinates (presume bottom left is (0,0)).  Then a series of two lines of commands for each robot. Presume that the robots move sequentially.
The first line is the current coordinates and heading in the format "1 2 N" for a robot at point (1,2) heading North
The second line is a series of character indicating the pattern of movement e.g. "LMLMLMMM".

The expected output is the final coordinates of each robot and its heading.

Test Input
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Expected output:
1 3 N
5 1 E


Further questions:

a. Make the robots move simultaneously. Avoid collisions.

b. Write the program so that each robot is a remote client. Your server program parses and sends data to each remote client and collects the responses back.

c. Presume that each robot has two on-board front cameras pointing 45degrees outwards from the heading of the robot. The cameras each photograph a grid point in front of them, every time the robot moves forward. Two photos are taken for each step moved by the robot. For each test input, the output should indicate the percentage of the field that has been photographed. Duplicate photos are OK. """
