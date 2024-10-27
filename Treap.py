class Node(object):
    def __init__(self,value:int,priority: int) -> None: 
        self.value = value
        self.left = None
        self.right = None
        self.priority = priority

def rotate_R(node:Node):
    s = node.left
    node.left = s.right
    s.right = node
    return s
def rotate_L(node:Node):
    s = node.right
    node.right = s.left
    s.left = node
    return s

def insert(node: Node,value:int,priority) -> Node:
    if node is None:
        return Node(value,priority)
    
    if value < node.value:
        node.left = insert(node.left,value,priority)
        if node.priority < node.left.priority:
            node = rotate_R(node)
    else:
        node.right = insert(node.right,value,priority)
        if node.priority < node.right.priority:
            node = rotate_L(node)
    return node

def find(node:Node,value: int) -> bool:
    if node is None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return find(node.left,value)
    elif node.value < value:
         return find(node.right,value)

def min_val(node:Node) -> Node:
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete(node:Node,value: int):
    if node is None:
        return
    if node.value > value:
        node.left = delete(node.left,value)
    elif node.value < value:
         node.right = delete(node.right,value)
    else:
        return _delete(node,value)
    return node

def _delete(node:Node,value:int):
    if node.left is None and node.right is None:
        return None
    if node.left is None:
        node = rotate_L(node)
    elif node.right is None:
        node = rotate_R(node)
    else:
        if node.left.priority > node.right.priority:
            node = rotate_R(node)
        else:
            node = rotate_L(node)
    return delete(node,value)
            
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
    msg = list(input().split())
    if msg[0] == 'print':
        res_inorder = []
        res_pre = []
        inorder(root)
        print("",*res_inorder)
        pre(root)
        print("",*res_pre)
    elif msg[0] == 'insert':
        root = insert(root,int(msg[1]),int(msg[2]))
    elif msg[0] == 'find':
        if find(root,int(msg[1])):
            print("yes")
        else:
            print("no")
    elif msg[0] == 'delete':
        root = delete(root,int(msg[1]))