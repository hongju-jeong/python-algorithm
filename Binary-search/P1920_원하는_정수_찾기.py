# https://www.acmicpc.net/problem/1920
import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int, input().split()))
A = sorted(A)


def binary_search(arr: list, target : int, start, end):
    while start<=end:
        pivot = (start + end)//2

        if (target == arr[pivot]):
            return 1
        elif target < arr[pivot]:
            end = pivot-1
        elif target > arr[pivot]:
            start = pivot+1

    return 0

for i in B:
    print(binary_search(A, i,0,len(A)-1))
