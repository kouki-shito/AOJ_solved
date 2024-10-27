class Node(object):
    def __init__(self,value:int) -> None: 
        self.value = value
        self.left = None
        self.right = None

def insert(node: Node,value:int) -> Node:
    if node is None:
        return Node(value)
    
    if value < node.value:
        node.left = insert(node.left,value)
    else:
        node.right = insert(node.right,value)
    return node



def inorder(node:Node) -> None:
    if node is not None:
        inorder(node.left)
        res_inorder.append(node.value)
        inorder(node.right)

def pre(node:Node) -> None:
    if node is not None:
        res_pre.append(node.value)
        pre(node.left)
        pre(node.right)

n = int(input())
root = None

for i in range(n):
    msg = input()
    if msg == 'print':
        res_inorder = []
        res_pre = []
        inorder(root)
        print("",*res_inorder)
        pre(root)
        print("",*res_pre)
    else:
        t, v = msg.split()
        if t == 'insert':
            root = insert(root,int(v))