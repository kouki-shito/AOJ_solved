class Node(object):
    def __init__(self):
        self.left = -1
        self.right = -1
        self.depth = -1
        self.parent = -1
        self.degree = 0
        self.height = 0
        self.sibling = -1
        self.type = ""

n = int(input())
tree = [Node() for _ in range(n)]

for _ in range(n):
    i, l, r = list(map(int,input().split()))
    if l == -1 and r == -1 :
        tree[i].type = "leaf"
        tree[i].height = 0
    else:
        tree[i].left = l
        tree[i].right = r
        if l != -1:
            tree[l].parent = i
        if r != -1:
            tree[r].parent = i
        tree[i].type = "internal node"

root_i = -1

for i in range(n):
    if tree[i].parent == -1:
        tree[i].type = "root"
        root_i = i
        break

def calc_depth(i,depth):
    tree[i].depth = depth
    height = 0
    if tree[i].type == "leaf":
        tree[i].height = 0
        return 1
    if tree[i].left != -1:
        tmp_hl = calc_depth(tree[i].left, depth + 1) # 再起でdepth付与
        height = max(height, tmp_hl)
    if tree[i].right != -1:
        tmp_hr = calc_depth(tree[i].right, depth + 1) # 再起でdepth付与
        height = max(height, tmp_hr)
    tree[i].height = height
    return height + 1

for i in range(n):
    if tree[i].left == -1 and tree[i].right == -1:
        pass
    elif tree[i].left != -1 and tree[i].right != -1:
        tree[i].degree = 2
    else:
        tree[i].degree = 1
    
for i in range(n):
    if tree[i].left != -1 and tree[i].right != -1:
        tree[tree[i].left].sibling = tree[i].right
        tree[tree[i].right].sibling = tree[i].left


calc_depth(root_i,0)

for i,node in enumerate(tree):
    print(f"node {i}: parent = {node.parent}, sibling = {node.sibling}, degree = {node.degree}, depth = {node.depth}, height = {node.height}, {node.type}")