class Node(object):
    def __init__(self):
        self.idx = 0
        self.left = -1
        self.right = -1
        self.parent = -1

n = int(input())

tree = [Node() for _ in range(n)]
res_pre = []
res_inorder = []
res_post = []

for _ in range(n):
    i, l, r = list(map(int,input().split()))
    tree[i].idx = i
    tree[i].left = l
    tree[i].right = r

    if tree[i].left != -1:
        tree[l].parent = i
    if tree[i].right != -1:
        tree[r].parent = i

root_i = -1

for i in range(n):
    if tree[i].parent == -1:
        root_i = i
        break

def calc_pre(i):
    res_pre.append(tree[i].idx) ## pre
    if tree[i].left != -1:
        calc_pre(tree[i].left)
    if tree[i].right != -1:
        calc_pre(tree[i].right)

def calc_inorder(i):
    if tree[i].left != -1:
        calc_inorder(tree[i].left)
    res_inorder.append(tree[i].idx) ## in
    if tree[i].right != -1:
        calc_inorder(tree[i].right)

def calc_post(i):
    if tree[i].left != -1:
        calc_post(tree[i].left)
    if tree[i].right != -1:
        calc_post(tree[i].right)
    res_post.append(tree[i].idx) ## post

calc_pre(root_i)
calc_inorder(root_i)
calc_post(root_i)

print("Preorder")
print("",*res_pre)
print("Inorder")
print("",*res_inorder)
print("Postorder")
print("",*res_post)
