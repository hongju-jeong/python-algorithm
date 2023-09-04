# https://school.programmers.co.kr/learn/courses/30/lessons/43105
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    D = [[0 for j in range(i)] for i in range(1,len(triangle)+1)]
    
    D[0][0] = triangle[0][0]
    
    for i in range(1,len(triangle)):
        for j in range(0,len(triangle[i])):
            if(j == 0):
                D[i][j] = D[i-1][j]+triangle[i][j]
                continue
            if(j == len(triangle[i])-1):
                D[i][j] = D[i-1][j-1] + triangle[i][j]
                continue
            
            D[i][j] = max(D[i-1][j-1]+triangle[i][j],D[i-1][j]+triangle[i][j])
            
    answer = max(D[len(triangle)-1])
    
    
    
    return answer


print(solution(triangle))
