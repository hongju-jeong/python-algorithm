import sys
import bisect

input = sys.stdin.readline

N = int(input())

CAList = list(map(int,input().split()))
#CAList = sorted(CAList)
CAList.sort()
cache = set(CAList)
count = 0
right = 0
left = 0
for i in range(0,len(CAList)-3):
    for j in range(i+1,len(CAList)-2):
        k = (CAList[i]+CAList[j])*-1
        if k in cache:
            count += bisect.bisect_right(CAList[j+1:len(CAList)-1],k)-bisect.bisect_left(CAList[j+1:len(CAList)-1],k)

print(count)