class Node(object):
    def __init__(self):
        self.children = []
        self.depth = -1
        self.parent = -1
        self.type = ""

n = int(input())
tree = [Node() for _ in range(n)]

for _ in range(n):
    i, k, *cl = list(map(int,input().split()))
    if k == 0:
        tree[i].type = "leaf"
    else:
        tree[i].children = cl
        for c in cl:
            tree[c].parent = i
        tree[i].type = "internal node"

root_i = -1

for i in range(n):
    if tree[i].parent == -1:
        tree[i].type = "root"
        root_i = i
        break

def calc_depth(i,depth):
    tree[i].depth = depth
    for chil in tree[i].children:
        calc_depth(chil, depth + 1) # 再起でdepth付与

calc_depth(root_i,0)

for i,node in enumerate(tree):
    print(f"node {i}: parent = {node.parent}, depth = {node.depth}, {node.type}, {node.children}")