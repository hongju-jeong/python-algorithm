# https://www.acmicpc.net/problem/2792
import sys
input = sys.stdin.readline

N, M = map(int, input().split())


jewelryList = [0]*M
for i in range(M):
    jewelryList[i] = int(input())

start = 1
end = max(jewelryList)

while(start<=end):
    pivot = (start+end)//2

    divideNum = 0 
    for jewelry in jewelryList:
        if(jewelry%pivot == 0):
            divideNum = divideNum + (jewelry//pivot)
        else:
            divideNum = divideNum + (jewelry//pivot) + 1
    if(divideNum > N):
        start = pivot+1
    else:
        end = pivot-1

print(start)

