import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lectureList = list(map(int, input().split()))

start = max(lectureList)
end = sum(lectureList)

def is_correct_bluelay(MSize):
    count = 0
    sum = 0
    for i in range(0,len(lectureList)):
        sum += lectureList[i]
        if(sum>MSize):
            count +=1
            sum = lectureList[i]

    count +=1

    return count
        

pivot = 0
correctPivot = 0
while(start<=end):
    pivot = (start+end)//2
    if(is_correct_bluelay(pivot) == M):
        end = pivot-1
    elif(is_correct_bluelay(pivot) < M):
        end = pivot-1
    else:
        start = pivot+1

print(start)

## 다시풀기 ;;