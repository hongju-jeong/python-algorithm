# https://www.acmicpc.net/problem/1325

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

B = [[] for _ in range(N+1)]

visited_num = [0]*(N+1)

for i in range(M):
    E, S = map(int,input().split())
    B[S].append(E)
    
def BFS(v):
    count = 0
    visited = [-1]*(N+1)
    queue = deque()
    queue.append(v)
    visited[v] += 1
    count += 1
    while queue:
        new_Node = queue.popleft()
        for i in B[new_Node]:
            if(visited[i] == -1):
                visited[i] +=1
                queue.append(i)
                count +=1
    
    return count

for i in range(N+1):
    count = BFS(i)
    visited_num[i] = count
    
max_num = max(visited_num)

answer = []
for i in range(N+1):
    if(visited_num[i] == max_num):
        answer.append(i)
        
for i in answer:
    print(i,end=" ")
        
# 시간초과
#PyPy3는 시간초과 안나는데 Python3는 시간초과 남


                
            
    

