import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = []
preS = []
for i in range(N):
    word = input()
    S.append(word[:-1])
for i in range(M):
    word = input()
    preS.append(word[:-1])
    
S = sorted(S)


def preS_search(word):
    
    start = 0
    end = N-1
    while(start<=end):
        pivot = (start+end)//2
        
        wordFind = 99
        wordFind = S[pivot].find(word)
        
        if(wordFind != 0):
            if(word > S[pivot]):
                start = pivot+1
            elif(word < S[pivot]):
                end = pivot-1
        else:
            return True
        
    return False

count = 0
for word in preS:
    if(preS_search(word) == True):
        count +=1
    
print(count)


