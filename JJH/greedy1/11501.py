
from sys import stdin
input = stdin.readline

t = int(input())

for _ in range(t):  
    n = int(input())
    arr = list(map(int,input().split()))
    e = 0
    cnt = 0 
    for i in range(n-1,-1,-1):
        e = max(e, arr[i])
        cnt += e - arr[i]
    print(cnt)
