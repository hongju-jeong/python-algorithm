https://www.acmicpc.net/problem/11053
import sys
input = sys.stdin.readline

N = int(input())
D = [0]*(N)
P = list(map(int, input().split()))
D[N-1] = 1
for i in range(N-2,-1,-1):
    big = 0
    if(P[i]>P[i+1] or P[i] < P[i+1]):
        for j in range(i,N):
            if(P[i]<P[j] and big < D[j]):
                big = D[j]
        D[i] = big+1
    else:
        D[i] = D[i+1]


print(max(D))

        
