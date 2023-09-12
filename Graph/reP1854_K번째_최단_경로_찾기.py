# https://www.acmicpc.net/problem/1854
# dijkstra

# import sys
# import heapq

# input = sys.stdin.readline

# N,M,K = map(int, input().split())

# A = [[] for _ in range(N+1)]

# visited = [-1]*(N+1)

# for _ in range(M):
#     start, end, weight = map(int, input().split())
#     A[start].append([end,weight])

# distance_each_node = [[] for _ in range(N+1)]
# distance_each_node_len = [0]*(N+1)
# distances = [sys.maxsize]*(N+1)
# queue = []

# start_Node = 1
# distances[start_Node] = 0

# heapq.heappush(queue,[distances[start_Node], start_Node])


# while queue:
#     curr_dist, curr_dest = heapq.heappop(queue)
    
#     if( (-1 in visited[1:]) == False):
#         count = 0
#         for dist_each_node in distance_each_node_len:
#             if(dist_each_node != 0 and dist_each_node<K):
#                 count +=1
        
#         if count == 0:
#             break
        
#     visited[curr_dest] +=1
      
#     for next_dest, next_dist in A[curr_dest]:
#         distance = next_dist + curr_dist
#         if(len(distance_each_node[next_dest])>=K):
#             currvalue = heapq.heappop(distance_each_node[next_dest])
#             if(distance < -currvalue):
#                 heapq.heappush(distance_each_node[next_dest], -distance) 
#             else:
#                 heapq.heappush(distance_each_node[next_dest], currvalue) 
#         else:
#             heapq.heappush(distance_each_node[next_dest], -distance)
#         distance_each_node_len[next_dest] +=1
        
#         #if(distance < distances[next_dest]):
#         distances[next_dest] = distance
#         heapq.heappush(queue, [distance, next_dest])

# #print(distance_each_node)
# for dist_list in distance_each_node[1:]:
#     if(len(dist_list) >= K):
        
#         answer = heapq.heappop(dist_list)
#         print(-answer)
#     else: print(-1)

#           메모리 초과

import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())

A = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    A[start].append([end, weight])
    
distance = [[sys.maxsize]*K for _ in range(N+1)]


queue = [[0,1]]
distance[1][0] = 0

while queue:
    curr_dist, curr_dest = heapq.heappop(queue)
    for new_dest, new_dist in A[curr_dest]:
        cost = curr_dist + new_dist
        if(distance[new_dest][K-1] > cost):
            distance[new_dest][K-1] = cost
            distance[new_dest].sort()
            heapq.heappush(queue, [cost, new_dest])
            
for i in range(1, N+1):
    if distance[i][K-1] == sys.maxsize:
        print(-1)
    else: print(distance[i][K-1])