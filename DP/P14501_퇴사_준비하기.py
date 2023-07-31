import sys
input = sys.stdin.readline

N = int(input())

T = [0]*(N+1)
P = [0]*(N+1)

D = [0]*(N+2)

for i in range(1,N+1):
    T[i],P[i] = map(int,input().split())


# 오늘 시작하는 상담이 퇴사일까지 끝나지 않은 경우 그 다음날의 최대값이 값이라는 것을 고려하지 않음
"""
for i in range(N,0,-1):
    if(i+T[i]<N+2):
        D[i] = max(D[i+1],D[i+T[i]]+P[i])
"""
for i in range(N,0,-1):
    if(i+T[i]>N+1):
        D[i] = D[i+1]
    else:
        D[i] = max(D[i+1],D[i+T[i]]+P[i])

# 그리고 D[1] 만해도 됨
"""
print(max(D))
"""
print(D[1])

