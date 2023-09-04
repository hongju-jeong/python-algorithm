<<<<<<< HEAD
"""
import sys
=======
# https://www.acmicpc.net/problem/1715

import sys
import heapq
>>>>>>> d064de1e4f97f6e8902088e46fd0d1355ef2e432

input = sys.stdin.readline

N = int(input())
<<<<<<< HEAD

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
    
=======
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
>>>>>>> d064de1e4f97f6e8902088e46fd0d1355ef2e432
