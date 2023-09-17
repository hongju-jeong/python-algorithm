# https://www.acmicpc.net/problem/1068

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

Tree = [[] for _ in range(N)]

input_Node = list(map(int, input().split()))

rootNode = 0
for index, node in enumerate(input_Node):
    if(node == -1):
        rootNode = index
    else:
        Tree[node].append(index)

leaf_count = 0
for i in range(len(Tree)):
    if(len(Tree[i]) == 0):
        leaf_count +=1


remove_Node = int(input())

for nodes in Tree:
    if(remove_Node in nodes and len(nodes) == 1):
        leaf_count +=1
    

queue = deque()

queue.append(remove_Node)

while queue:
    new_Node = queue.pop()
    
    if(len(Tree[new_Node]) == 0):
        leaf_count -= 1
    else:
        for i in Tree[new_Node]:
            queue.appendleft(i)

print(leaf_count)


