# https://www.acmicpc.net/problem/10816
import sys
input = sys.stdin.readline

N = int(input())
NList = list(map(int,input().split()))
M = int(input())
MList = list(map(int,input().split()))

def binary_search(arr, target, _start, _end):
    start = _start
    end = _end
    leftmost = -1
    rightmost = -1
    while(start<=end):
        pivot = (start+end)//2
        if(target == arr[pivot]): 
            leftmost = pivot
            end = pivot-1
        elif(target > arr[pivot]):
            start = pivot+1
        else:
            end = pivot-1

    start = _start
    end = _end
    
    while(start<=end):
        pivot = (start+end)//2
        if(target == arr[pivot]):
            rightmost = pivot
            start = pivot+1
        elif(target > arr[pivot]):
            start = pivot+1
        else:
            end = pivot-1
    if(leftmost != -1 and rightmost != -1):
        return rightmost-leftmost+1
    else:
        return 0

NList = sorted(NList)

for MNumber in MList:
    print(binary_search(NList,MNumber,0,N-1),end=' ')
