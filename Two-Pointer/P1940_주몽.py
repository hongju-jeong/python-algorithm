import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

elementList = list(map(int,input().split()))

start = 0
end = len(elementList)-1

elementList.sort()
sum = 0
count = 0
while(start<end):
    sum = elementList[start]+elementList[end]
    if(sum < M):
        start+=1
    elif(sum > M):
        end-=1
    else:
        count+=1
        start+=1
print(count)