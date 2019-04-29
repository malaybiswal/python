class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node=Node(new_data)
        #print('new_node:',new_node)
        new_node.next=self.head
        #print('self head1:',self.head)
        self.head=new_node
        #print('self head2:',self.head)

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    # Given a reference to the head of a list and a key,
    # delete the first occurence of key in linked list
    def deleteNode(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data==key):#head node is key
                self.head=temp.next
                temp=None
                return
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if(temp.data == key):
                break
            print('tempDATA:',temp.data)
            prev=temp
            temp=temp.next

        if(temp==None):# if key was not present in linked list
            return
        prev.next=temp.next# Unlink the node from linked list
        temp=None



if __name__=='__main__':
    llist=LinkedList()
    #llist.head = Node(1)
    #second = Node(2)
    #third = Node(3)
    #llist.head.next = second
    #second.next = third
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.printList()
    llist.deleteNode(2)
    print('--------------------')
    llist.printList()
