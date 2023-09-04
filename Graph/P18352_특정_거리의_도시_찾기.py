# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

A = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
answer = []

for i in range(M):
    S,E = map(int, input().split())
    A[S].append(E)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] +=1
    while queue:
        new_Node = queue.popleft()
        for i in A[new_Node]:
            if(visited[i] == -1):
                visited[i] = visited[new_Node] + 1
                queue.append(i)
                
BFS(X)

for i in range(N+1):
    if (visited[i] == K):
        answer.append(i)


if not answer:
    print(-1)        
else: 
    answer.sort()
    for i in answer:
        print(i)