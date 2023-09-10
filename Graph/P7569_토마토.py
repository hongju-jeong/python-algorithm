# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

box = [[] for _ in range(H)]


# 패딩을 쉽게 하는 방법 없을까

queue = deque()
zero_count = 0
day_count = 0

for i in range(H):
    for j in range(N):
        M_row = list(map(int,input().split()))
        box[i].append(M_row)
        for k in range(M):
            if(box[i][j][k] == 1):
                queue.append([i,j,k])   # 객체를 넘기면 객체 값이 바뀐다
            elif(box[i][j][k] == 0):
                zero_count +=1

#print(queue)
queue.appendleft("dayEnd")

while queue:
    new_Node = queue.pop()
    if (new_Node == "dayEnd"):
        if(len(queue) == 0):
            break
        else:
            queue.appendleft("dayEnd")
            day_count +=1
    else:
        i,j,k = new_Node
        #print("newNode:",i,j,k)
        
        # upnode
        if(i != (H-1)):
            if(box[i+1][j][k] == 0):
                box[i+1][j][k] = 1
                zero_count -=1
                queue.appendleft([i+1,j,k])
        
        # downnode
        if(i != 0):
            if(box[i-1][j][k] == 0):
                box[i-1][j][k] = 1
                zero_count -=1
                queue.appendleft([i-1,j,k])
        
        # frontnode
        if(j != N-1):
            if(box[i][j+1][k] == 0):
                box[i][j+1][k] = 1
                zero_count -=1
                queue.appendleft([i,j+1,k])
        # backnode
        if(j != 0):
            if(box[i][j-1][k] == 0):
                box[i][j-1][k] = 1
                zero_count -=1
                queue.appendleft([i,j-1,k])

        # leftnode
        if(k != 0):
            if(box[i][j][k-1] == 0):
                box[i][j][k-1] = 1
                zero_count -=1
                queue.appendleft([i,j,k-1])
        
        # rightnode
        if(k != M-1):
            if(box[i][j][k+1] == 0):
                box[i][j][k+1] = 1
                zero_count -=1
                queue.appendleft([i,j,k+1])

#print(zero_count)    
if(zero_count != 0):
    print(-1)
else:
    print(day_count)
    





        





