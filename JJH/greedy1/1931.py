from functools import cmp_to_key
from sys import stdin
input =  stdin.readline

def cmp(a, b):
    if(a[1]==b[1]): # 
        if a[0] > b[0]: # 왼쪽이 더 클 때 
            return 1  # true false not -> 1, 0, -1 
        elif a[0] == b[0]: 
            return 0 # 그대로 
        else:
            return -1  # 오른쪽이 더 클 때 
    else:
        if a[1] > b[1]:
            return 1
        else: # elif 
            return -1

n = int(input()) # test case 

schedule = []

for _ in range(n):
    start, end = map(int,input().split())
    schedule.append([start,end])

schedule.sort(key = cmp_to_key(cmp))
end = -1
cnt = 0

for i in range(n):
    if(end <= schedule[i][0]):
        end = schedule[i][1]
        cnt += 1

print(cnt)


