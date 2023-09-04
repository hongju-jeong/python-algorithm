# https://www.acmicpc.net/problem/1912
import sys
input = sys.stdin.readline

N = int(input())

D = [0]*(N)
P = [0]*(N)

num = input().split()
for i in range(0,N):
    P[i] = int(num[i])

for i in range(N-1,-1,-1):
    if(i == N-1):
        D[i] = P[i]
    else:
        D[i] = max(D[i+1]+P[i],P[i])

print(max(D))

