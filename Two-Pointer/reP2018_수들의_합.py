import sys
input = sys.stdin.readline

N = int(input())

start = 1
end = 1
sum = 1
count = 0
while(end<=N):
    if(sum < N):
        end +=1
        sum += end
    elif(sum > N):
        sum -= start
        start +=1
    else:
        count += 1
        end +=1
        sum = sum + end - start
        start +=1
        

print(count)