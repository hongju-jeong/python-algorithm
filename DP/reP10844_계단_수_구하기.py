
"""     
import sys
input = sys.stdin.readline

N = int(input())

D  = {0:[]}

for i in range(1,10):
    D[0].append(i)
    
#D[0] = set(D[0])
 
def sum(d1 : list,d2 : list):
    d3 = []
    for i in range(len(d1)):
        for j in range(len(d2)-1,-1,-1):
            cnt = 1
            temp_d2 = d2[j]
            while(temp_d2//10 != 0): 
                cnt += 1
                temp_d2 = temp_d2//10
            if(d1[i] % 10 == 0 and temp_d2 == 1):
                d3.append(d1[i]*(10 ** (cnt)) + d2[j])
                continue
            if(d1[i] % 10 == 9 and temp_d2 == 8):
                d3.append(d1[i]*(10 ** (cnt)) + d2[j])
                continue
                
            for k in range(1,9):
                if(d1[i] % 10 == k and (temp_d2 == k+1 or temp_d2 == k-1)):
                    d3.append(d1[i]*(10 ** (cnt)) + d2[j])
                    continue
                    
    
    d3_set = set(d3)
    d3 = list(d3_set)
    
    return d3

D[1] = sum(D[0],D[0])
D[1].append(10)
D[1] = sorted(D[1])
print(D[1])

# #make dict
# for i in range(1,N):
#     D[i+1] = []
#     for j in range(0,i+1):
#         k = i-j
#        # print(j," ",k)
#         D[i+1].extend(sum(D[j],D[k]))
        
#     D_set = set(D[i+1])
#     D[i+1] = list(D_set)
            

# print(len(D[N-1]))
"""
# ----------------------------------------------------------------------
# 메모리에 저장해놓고 자리수 +1 -1 로 비교해서 풀려다가 시간초과가 난 문제
# ----------------------------------------------------------------------

import sys
input = sys.stdin.readline

N = int(input())

D = [[0 for j in range(10)] for i in range(N+1)]

for i in range(1,10):
    D[1][i] = 1
    
for i in range(2,N+1):
    for j in range(0,10):
        if(j == 0):
            D[i][j] = D[i-1][j+1]
        elif(j == 9):
            D[i][j] = D[i-1][j-1]
        else:
            D[i][j] = D[i-1][j-1] + D[i-1][j+1]

sum = 0        
for i in range(len(D[N])):
    sum += D[N][i]
    
print(sum%1000000000)
            