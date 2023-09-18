# https://www.acmicpc.net/problem/1991

import sys

input = sys.stdin.readline


N = int(input())

Tree = dict()

for _ in range(N):
    parent, left, right = input().strip().split()
    Tree[parent] = {"left" : left, "right" : right}
    
    
# 전위 순회
pre_answer = []
def preorder(v):
    if(v != "."):
        pre_answer.append(v)
        preorder(Tree[v]["left"])
        preorder(Tree[v]["right"])
    
preorder("A")

for char in pre_answer:
    print(char,end="")
print()
    
# 중위 순회
inorder_answer = []
def inorder(v):
    if(v != "."):
        inorder(Tree[v]["left"])
        inorder_answer.append(v)
        inorder(Tree[v]["right"])
        
inorder("A")

for char in inorder_answer:
    print(char,end="")
print()

# 후위 순회
postorder_answer = []
def postorder(v):
    if(v != "."):
        postorder(Tree[v]["left"])
        postorder(Tree[v]["right"])
        postorder_answer.append(v)
        
        
postorder("A")

for char in postorder_answer:
    print(char,end="")