# https://www.acmicpc.net/problem/1707
# 이분그래프는 두개의 색으로 인접하지 않고 색칠할 수 있는 것
import sys
from collections import deque
input = sys.stdin.readline

K = int(input())

answer = []

for _ in range(K):
    V, E = map(int,input().split())
    A = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int,input().split())
        A[start].append(end)
        A[end].append(start)

    visited_color = [-1]*(V+1)

    queue = deque()
    color = 0
    is_bi_graph = True
    for i in range(len(A)):
        if(visited_color[i] != -1):
            continue
        else:
            color =0

        queue.append(i)
        visited_color[i] = color%2
        color +=1

        while queue:
            if(is_bi_graph == False):
                break
            new_node = queue.popleft()
            for j in A[new_node]:
                if(visited_color[j] == -1):
                    visited_color[j] = (visited_color[new_node]+1)%2
                    queue.append(j)
                elif(visited_color[j] != visited_color[new_node]):
                    continue
                else:
                    is_bi_graph = False
                    break
        
        if(is_bi_graph == False):
            answer.append("NO")
            break

    if(is_bi_graph ==True):
        answer.append("YES")

for i in answer:
    print(i)

