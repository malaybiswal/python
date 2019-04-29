
import time
def shuffle(deck):
    #deck=[]
    table=[]
    count=0;tablecount=0
    #for i in range(1,6):
        #deck.insert(i-1,i)

    #print(deck)
    while(len(deck)>0):

        if(count%2==0):
            c=deck[0]
            #print("PUSHING INTO TABLE count is:",count,"card is:",c)
            table.insert(0,c)
            tablecount+=1
            deck.pop(0)
            #print(deck)
            #print(table)
        else:
            temptable=deck.pop(0)
            deck.append(temptable)
            #deck.insert(0,temptable)

            #print("PUSHING INTO END OF DECK count is:",count,"card is:",temptable)
            #print(deck)
            #print(table)
        count+=1
    return table

start_time = time.time()
inc=0;mode=0
deck=[]
mode=input('Enter number of cards you want to sort:')
try:
    mode=int(mode)
    mode+=1
except ValueError:
    print ("Not a number")
for i in range(1,mode):
    deck.insert(i-1,i)
deck1=deck.copy()
table=shuffle(deck)
print("DECK:",deck1)
#print("TABLE after 1st pass:",table)
while(deck1!=table):
    inc+=1
    table=shuffle(table)
    #print("TABLE after ",inc+1," pass:",table)
    #if(inc%10000==0):
        #print("TABLE after ",inc+1," pass:",table)
print(table)
print("It took ",inc+1, " passes to get the card in original order")
print("--- %s seconds ---" % (time.time() - start_time))
#print("TABLE HAS cards :",shuffle(deck))
#print(deck)
