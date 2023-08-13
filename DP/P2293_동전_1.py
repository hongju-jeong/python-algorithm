import sys
input = sys.stdin.readline

N, K = map(int,input().split())
coin = [0]*K
for i in range(K):
    coin[i] = int(input())



