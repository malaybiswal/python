class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        print("----------------",key)
def insert(root,node):
    if root is None:
        root=node
        print("****************")
    else:
        if root.val < node.val:
            print("+++++++++++++++++++",root.val,'-',node.val)
            if root.right is None:
                root.right=node
                print(root.val,"root.val < node.val IN IF",node.val,"-root.right-",root.right)
            else:
                insert(root.right,node)
                print(root.val,"root.val < node.val IN ELSE",node.val)
        else:
            print("^^^^^^^^^^^^^^^^^^^^",root.val,'-',node.val)
            if root.left is None:
                root.left = node
                print(root.val,"root.val > node.val IN IF",node.val,"-root.left-",root.left)
            else:
                insert(root.left,node)
                print(root.val,"root.val > node.val IN ELSE",node.val)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
r=Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))

# Print inoder traversal of the BST
inorder(r)
