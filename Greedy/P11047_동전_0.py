# https://www.acmicpc.net/problem/11047
import sys

input = sys.stdin.readline

N, K = map(int,input().split())

coins = []
for i in range(N):
    coin = int(input())
    coins.append(coin)
count = 0
while(K > 0):
    minIndex, minQuo = 0 , 99999999
    for i in range(N):
        if(K//coins[i] < minQuo and K//coins[i] > 0):
            minIndex = i
            minQuo = K//coins[i]
    K = K- (coins[minIndex]*minQuo)
    count += minQuo

print(count)


