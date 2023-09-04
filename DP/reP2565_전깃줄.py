# https://www.acmicpc.net/problem/2565
# import sys
# input = sys.stdin.readline

# N = int(input())

# lineRangeList=[]

# for i in range(N):
#     lineRangeList.append(list(map(int,input().split())))


# removeLineCount = 0
# for lineRange1 in enumerate(lineRangeList):
#     for lineRange2 in enumerate(lineRangeList):

#         if(lineRange1[1][0] < lineRange2[1][0]):
#             if(lineRange1[1][1] < lineRange2[1][1]):
#                 continue
#             else :
#                 removeLineCount +=1
#                 break
#         else:
#             continue


# print(removeLineCount)

import sys
input = sys.stdin.readline

N = int(input())
D = [0]*(N+1)
lineList = [0]*501

for i in range(N):
    a ,b = map(int,input().split())
    lineList[a] = b

while(0 in lineList):
    lineList.remove(0)

D[N-1] = 1
for i in range(N-2,-1,-1):
    big = 0
    if(lineList[i]>lineList[i+1] or lineList[i] < lineList[i+1]):
        for j in range(i,N):
            if(lineList[i]<lineList[j] and big < D[j]):
                big = D[j]
        D[i] = big+1
    else:
        D[i] = D[i+1]

print(N-max(D))


## 이거 DP로 제대로 푼건지 P11053 가장 긴 증가하는 부분 수열 문제 다시보기

        




