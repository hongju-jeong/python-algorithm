# https://www.acmicpc.net/problem/1253
import sys

input = sys.stdin.readline

N = int(input())
AList = list(map(int,input().split()))

AList.sort()
count=0

for i in range(0,len(AList)):
    target = AList[i]
    start = 0
    end = len(AList)-1
    sum = 0
    find = False
    while(start<end):
        if(start == i):
            start+=1
            continue
        elif(end == i):
            end -=1
            continue
        sum = AList[start]+AList[end]
        if(sum>target):
            end -=1
        elif(sum<target):
            start +=1
        else:
            find = True
            break
    if(find == True):
        count+=1

print(count)

# 자연수 인줄 알고 오래걸림
