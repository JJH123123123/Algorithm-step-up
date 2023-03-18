from sys import stdin
input = stdin.readline

n = int(input()) # 로프의 개수 

ropes = [] # 로프의 배열 

for i in range(n):
    ropes.append(int(input())) # rope input 

# 여기가 핵심 
ropes.sort(reverse = True) # 내림차순 정렬

cnt = 0
for i in range(n):
    if (cnt < (i+1)*ropes[i]): # 
        cnt = (i+1)*ropes[i] 

print(cnt)
