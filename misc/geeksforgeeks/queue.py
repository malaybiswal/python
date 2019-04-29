#Implementing queue
import sys
queue = ['A','B','C','D','E','F']

def view():
    for x in range(len(queue)):
        print(queue[x])
        
def push():
    item = input("Enter item to Push to queue:")
    queue.append(item)

def pop():
    item=queue.pop(0)
    print("You just popped out item:", item)
    
while True:
    print("")
    print("Python implementation of queue")
    print("******************************")
    print("1.View Queue")
    print("2.Push to Queue")
    print("3.Pop Queue")
    print("******************************")
    print("")
    try:
        menu_choice = int(input("Eneter your choice:"))
    except ValueError:
        print("EXITING AS NO INPUT.")
        sys.exit(1)
    print("")
    print("")
    
    
    
    if menu_choice == 1:
        view()
    elif menu_choice == 2:
        push()
    elif menu_choice == 3:
        pop()
        
    else:
        print("EXITING..")