import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = k
"""
while(start<=end):
    pivot = (start+end)//2

    cnt = 0
    for i in range(1,pivot+1):
        for j in range(1,N+1):
            if((i//j) <= N and (i//j) > 0 and (i%j) == 0):
                cnt+=1
    # print("pivot:", pivot)
    # print("cnt:", cnt)
    if(cnt < k):
        start = pivot+1
    elif(cnt > k):
        end = pivot-1
"""

while(start<=end):
    pivot = (start+end)//2
    cnt=0
    for i in range(1,N+1):
        cnt += min(pivot//i,N)
    #print("cnt",cnt)
    if(cnt <k):
        start = pivot+1
    else:
        end = pivot-1
print(start)