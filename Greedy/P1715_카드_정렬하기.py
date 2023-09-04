# https://www.acmicpc.net/problem/1715
"""
import sys
import heapq1355ef2e432

input = sys.stdin.readline

N = int(input())

cardNums = [0]*N

for i in range(N):
    cardNums[i] = int(input())
    
cardNums.sort()

if(N == 1):
    minCompare = cardNums[0]
else:
    minCompare = cardNums[0]+cardNums[1]
for i in range(2,N):
    minCompare += minCompare+cardNums[i]
    

print(minCompare)
"""
# ============ 출력 초과 =================

import sys
import heapq
input = sys.stdin.readline

N = int(input())

cardNums = [0]*N
for i in range(N):
    cardNums[i] = int(input())

heapq.heapify(cardNums)

count = 0
if(N == 1):
    print(0)
else:
    while(len(cardNums)>1):
        A = heapq.heappop(cardNums)
        B = heapq.heappop(cardNums)
        count += A+B
        ABsum = A+B
        heapq.heappush(cardNums,ABsum)

    print(count)
    