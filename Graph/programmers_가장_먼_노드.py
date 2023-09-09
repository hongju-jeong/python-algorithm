#https://school.programmers.co.kr/learn/courses/30/lessons/49189
from collections import deque

def BFS(v,n,A):
    visited = [-1]*(n+1)
    queue = deque()
    queue.append(v)
    visited[v] +=1
    while queue:
        new_Node = queue.popleft()
        for i in A[new_Node]:
            if(visited[i] == -1):
                visited[i] = visited[new_Node]+1
                queue.append(i)
                
    max_num = max(visited)
    count = 0
    for i in range(n+1):
        if(visited[i] == max_num):
            count+=1
    return count

def solution(n, edge):
    
    A = [[] for _ in range(n+1)]
    
    for i in edge:
        S, E = i[0], i[1]
        A[S].append(E)
        A[E].append(S)
        
    
    return BFS(1,n,A)


    
    