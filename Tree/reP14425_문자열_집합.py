# https://www.acmicpc.net/problem/14425
# dictionary로 구현하기
# Class 로 구현하기
# set으로 구현하기
# list로 구현하기

# Trie 구조
"""
import sys

input = sys.stdin.readline

N,M = map(int, input().split())

class Node():
    
    def __init__(self, _isEnd):
        self.isEnd = _isEnd
        self.childNode = {}
    
    
class Trie():
    
    def __init__(self):
        self.root = Node(None)
        
    def insert(self, string):
        nowNode = self.root
        temp_length = 0
        for char in string:
            if char not in nowNode.childNode:
                nowNode.childNode[char] = Node(char)
                
            nowNode = nowNode.childNode[char]
            temp_length +=1
            if temp_length == len(string):
                nowNode.isEnd = True
                
    def search(self, string):
        nowNode = self.root
        temp_length = 0
        for char in string:
            if char in nowNode.childNode:
                nowNode = nowNode.childNode[char]
                temp_length +=1
                if temp_length == len(string) and nowNode.isEnd == True:
                    return True
            else:
                return False
            
        return False
    
    
myTrie = Trie()

for _ in range(N):
    word = input().strip()
    myTrie.insert(word)
    
    
result = 0
for _ in range(M):
    word = input().strip()
    if myTrie.search(word):
        result +=1
        
print(result)
    
"""

#List
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
textList = [input() for _ in range(N)]
count = 0

for _ in range(M):
    text = input()
    if text in textList:
        count +=1
        
print(count)

"""

#set
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
textList = set([input() for _ in range(N)])
count = 0

for _ in range(M):
    text = input()
    if text in textList:
        count +=1
        
print(count)
"""

#dictinary

import sys

input = sys.stdin.readline


N,M = map(int, input().split())

trie = dict()

for _ in range(N):
    word = input().strip()
    cur = trie
    for ch in word:
        if ch not in cur.keys():
            cur[ch] = dict()
        cur = cur[ch]
    cur['*'] = True
    
count =0

for _ in range(M):
    word = input().strip()
    cur = trie
    indict = True
    for ch in word:
        if ch not in cur.keys():
            indict = False
            break
        cur = cur[ch]
    if indict and '*' in cur.keys():
        count +=1
    
    
print(count)