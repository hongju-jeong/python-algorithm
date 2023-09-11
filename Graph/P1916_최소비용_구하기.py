# https://www.acmicpc.net/problem/1916
# dijkstra

import sys
import heapq

input = sys.stdin.readline
# sys.maxsize

N = int(input())
M = int(input())

A = [[] for i in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    A[start].append([end,weight])
    
visited = [-1]*(N+1)
distances = [sys.maxsize]*(N+1)

queue = []

start_Node, end_Node = map(int,input().split())

distances[start_Node] = 0
heapq.heappush(queue,[distances[start_Node], start_Node])

while queue:
    curr_distance, curr_destination = heapq.heappop(queue)
    if(visited[curr_destination] == -1):
        visited[curr_destination] = 0
        
        for next_Node, next_weight in A[curr_destination]:
            distance = curr_distance + next_weight
            if(distance < distances[next_Node]):
                distances[next_Node] = distance
                heapq.heappush(queue, [distance, next_Node])
                
print(distances[end_Node])
    
