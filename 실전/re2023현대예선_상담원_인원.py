#https://school.programmers.co.kr/learn/courses/30/lessons/214288

from itertools import product
from collections import deque

def solution(k, n, reqs):
    
    man_add_list = [0]*(k+1)
    min_delay = 99999999
    values = list(range(1, n + 1))
    result = []
    for combo in product(values, repeat=k):
        if sum(combo) == n:
            combo = deque(combo)
            combo.appendleft(0)
            combo = list(combo)
            result.append(combo)
    
    for queue in result:
        man_add_list = queue
        delay = scheduler(k,reqs, man_add_list)
        sum_delay = sum(delay)
        
        if(min_delay > sum_delay):
            min_delay = sum_delay
                             
    return min_delay

def scheduler(k,reqs, man_add_list):
    man_list = [[0] for _ in range(k+1)]
    delay = [0]*(k+1)
    
    for index, add_num in enumerate(man_add_list[1:k+1]):
        for _ in range(add_num-1):
            man_list[index+1].append(0)
        
    for req in reqs:
        for i in range(1,k+1):
            if(req[2] == i):
                min = 99999999
                min_index = 0
                for index, j in enumerate(man_list[i]):
                    if j < min:
                        min = j
                        min_index = index
                if man_list[i][min_index] == 0:
                    man_list[i][min_index] = req[0]+req[1]
                elif man_list[i][min_index] == req[0]:
                    man_list[i][min_index] += req[1]
                elif man_list[i][min_index] < req[0]:
                    man_list[i][min_index] = req[0]+req[1]
                else :
                    delay[i] += (man_list[i][min_index] - req[0])
                    man_list[i][min_index] += req[1]
    
    
    return delay

# 뒤에서 그리디로 풀어보기, 학생인원만큼 다채우고