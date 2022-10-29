import sys 

input=sys.stdin.readline

class Node:
    def __init__(self,item,left,right):
        self.item=item
        self.left=left
        self.right=right

def pre_order(node):
    print(node.item,end='')
    if node.left!=None:
        pre_order(tree[node.left])
    if node.right!=None:
        pre_order(tree[node.right])

def in_order(node):
    if node.left!=None:
        in_order(tree[node.left])
    print(node.item,end='')
    if node.right!=None:
        in_order(tree[node.right])

def post_order(node):
    if node.left!=None:
        post_order(tree[node.left])
    if node.right!=None:
        post_order(tree[node.right])
    print(node.item,end='')

n=int(input())
tree={}
for _ in range(n):
    root,left,right=input().split()
    if left=='.':
        left=None
    if right=='.':
        right=None
    tree[root]=Node(root,left,right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])