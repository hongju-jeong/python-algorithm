"""
import sys

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

cardNums = []
for i in range(N):
    cardNum = int(input())
    heapq.heappush(cardNums,cardNum)

minCompare = 0
preSum = 0
while len(cardNums) >0:
    if(i<2):
        cardNum = heapq.heappop(cardNums)
        minCompare += cardNum
        preSum = 
    
        

    
print(minCompare)
    
