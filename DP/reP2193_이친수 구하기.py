# https://www.acmicpc.net/problem/2193
import sys

input = sys.stdin.readline

N = int(input())
D = [-1]*(N+1)
D[0] = 0
D[1] = 1
 
for i in range(2, N+1):
     D[i] = D[i-2] + D[i-1]
     
print(D[N])


 # 피보나치 말고 다시 풀기
 
