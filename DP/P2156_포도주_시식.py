import sys
input = sys.stdin.readline

N = int(input())

D = [0]*(N+1)
P = [0]*(N+1)

for i in range(1,N+1):
    P[i] = int(input())

def max_wine(N):
    D[N] = P[N]
    if(N == 1):
        return D[N]
    D[N-1] = P[N]+P[N-1]
    if(N == 2):
        return D[N-1]
    
    D[N-2] = max(D[N]+P[N-2], D[N-1], P[N-2]+P[N-1])
    if(N == 3):
        return D[N-2]
    
    for i in range(N-3,0,-1):
        D[i] = max(P[i]+P[i+1]+D[i+3], D[i+2]+P[i], D[i+1])
    
    return D[1]




print(max_wine(N))
