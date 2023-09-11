# https://www.acmicpc.net/problem/1753
# dijkstra 기본문제
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

A = [[] for _ in range(V+1)]

start_Node = int(input())

for i in range(E):
    start, end, weight = map(int, input().split())
    A[start].append([end,weight])
    
visited = [-1]*(V+1)
distances = [999999]*(V+1)  #float('inf')

#dijkstra

distances[start_Node] = 0

queue = []
heapq.heappush(queue, [distances[start_Node], start_Node])

while queue:
    cur_distance, cur_destination = heapq.heappop(queue)
    #print(cur_distance, cur_destination)
    if(visited[cur_destination] == -1):
        visited[cur_destination] = 0
        
        #print(visited)
        
        for new_destination, new_distance in A[cur_destination]:
            distance = cur_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
                
for i in range(1,V+1):
    if(distances[i] == 999999):
        print('INF')
    else:
        print(distances[i])
