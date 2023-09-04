https://www.acmicpc.net/problem/3151
'''
import sys
import bisect
input = sys.stdin.readline

N = int(input())
CAList = list(map(int,input().split()))

CAList.sort()

count = 0
for i in range(len(CAList)-2):
    start = i+1
    end = N-1
    while(start<end):
        target = CAList[i]+CAList[start]+CAList[end]
        if(target > 0):
            end -= 1
        elif(target == 0):
            if(CAList[start]==CAList[end]):
                count += (end-start+1)*(end-start)//2
                break
            else:
                le = bisect.bisect_left(CAList,CAList[end])
                num_e = end-le+1
                rs = bisect.bisect_right(CAList,CAList[start])
                num_s = rs-start
                count += num_s*num_e
            start += num_s
            end -= num_e
        else:
            start +=1

print(count)
'''
# 시간초과


import sys
import bisect
input = sys.stdin.readline

N = int(input())
CAList = list(map(int,input().split()))

CAList.sort()

count = 0
for i in range(len(CAList)-2):
    start = i+1
    end = N-1
    while(start<end):
        target = CAList[i]+CAList[start]+CAList[end]
        if(target > 0):
            end -= 1
        elif(target == 0):
            if(CAList[start]==CAList[end]):
                count += (end-start+1)*(end-start)//2
                break
            else:
                is_end = CAList[end]
                e = 0
                while True:
                    if CAList[end] !=is_end:
                        break
                    else:
                        end -=1
                        e +=1
                is_start = CAList[start]
                s = 0
                while True:
                    if CAList[start] !=is_start:
                        break
                    else:
                        start +=1
                        s +=1
                count += s*e
        else:
            start +=1

print(count)
