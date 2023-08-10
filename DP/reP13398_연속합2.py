import sys
input = sys.stdin.readline

N = int(input())

D = [0]*(N)
P = [0]*(N)
D2 = [0]*(N)


num = input().split()
for i in range(0,N):
    P[i] = int(num[i])

upThanZero = 0
for i in range(N):
    if(P[i] > 0):
        upThanZero += 1
    
if(upThanZero > 0):

    flag = 0
    for i in range(N-1,-1,-1):
        if(i == N-1):
            D[i] = P[i]
            if(P[i] < 0):
                D2[i] = 0
                flag = 1
            else:
                D2[i] = P[i]
        else:
            D[i] = max(D[i+1]+P[i],P[i])
            if(flag == 0):
                if(D[i+1] == max(D[i+1]+P[i],P[i],D[i+1])):
                    D2[i] = max(D[i+1]+P[i],P[i],D[i+1])
                    flag = 1
            
            elif(flag == 1):
                D2[i] = max(D2[i+1]+P[i], P[i])
                if(D2[i] < max(D[i+1]+P[i],P[i],D[i+1])):
                    D2[i] = max(D[i+1]+P[i],P[i],D[i+1])
                


    if(flag == 0):
        print(max(D))
    else:
        print(max(D2))

else:
    print(max(P))

# DP로 다르게 풀어보기