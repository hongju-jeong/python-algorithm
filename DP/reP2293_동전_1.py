import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coin_list = [0]*(N)
for i in range(N):
    coin_list[i] = int(input())

D = [0]*(K+1)

D[0] = 1
    
for coin in coin_list:
    for i in range(0,K+1):
        if(i<coin):
            continue
        else:
            D[i] = D[i]+D[i-coin]
            
print(D[K])


# DP는 기존걸 쓸 수 있는지 체크를 하고 쓰려고 노력해야 한다
# 답이 안나올 땐 예제 원소를 하나씩 접근하면서 DP를 찾아보자