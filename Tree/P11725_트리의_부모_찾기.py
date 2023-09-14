# https://www.acmicpc.net/problem/11725

import sys
from collections import deque

input = sys.stdin.readline


N = int(input())

Tree = [[] for _ in range(N+1)]

answer = [-1]*(N+1)
visited = [-1]*(N+1)

for i in range(N-1):
    parent, child = map(int, input().split())
    Tree[parent].append(child)
    Tree[child].append(parent)
    
queue = deque()

queue.append(1)
visited[1] = 0

while queue:
    new_Node = queue.popleft()
    for i in Tree[new_Node]:
        if(visited[i] == -1):
            answer[i] = new_Node
            visited[i] = 0
            queue.append(i)
            
for i in answer[2:]:
    print(i)
    
 