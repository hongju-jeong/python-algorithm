# https://www.acmicpc.net/problem/1744

import sys
import heapq


input = sys.stdin.readline

N = int(input())

positiveHeap = []
negetiveHeap = []
positiveSum = 0
negetiveSum = 0

for i in range(N):
    num = int(input())
    if(num<=0):
        heapq.heappush(negetiveHeap,num)
    else:
        heapq.heappush(positiveHeap,(-num,num))

if(len(positiveHeap) ==1):
    positiveSum = positiveHeap[0][1]
else:
    while(len(positiveHeap)>1):
        A = heapq.heappop(positiveHeap)[1]
        B = heapq.heappop(positiveHeap)[1]
        if(A*B >= A+B):
            positiveSum += A*B
        else:
            positiveSum += A+B
        

    if(len(positiveHeap)==1):
        positiveSum += positiveHeap[0][1]

if(len(negetiveHeap) ==1):
    negetiveSum = negetiveHeap[0]
else:
    while(len(negetiveHeap)>1):
        A = heapq.heappop(negetiveHeap)
        B = heapq.heappop(negetiveHeap)
        negetiveSum += A*B

    if(len(negetiveHeap) ==1):
        negetiveSum += negetiveHeap[0]

print(negetiveSum+positiveSum)