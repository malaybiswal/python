# return Lowet Common ANcestor of nodes.
class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def lca(root,l,r):
    if root is None:
        return None
    elif(root.data>l and root.data>r):
        return lca(root.left,l,r)
    elif(root.data<l and root.data<r):
        return lca(root.right,l,r)
    else:
        return root
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
n1 = 10 ; n2 = 14
t = lca(root, n1, n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))
n1=4;n2=14
t=lca(root,n1,n2)
print ("LCA of %d and %d is %d" %(n1, n2, t.data))
