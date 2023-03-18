from sys import stdin
import heapq

input = stdin.readline

n, m  = map(int, input().split())
st = list(map(int,input().split()))

myheap = [] 
for i in range(n):
    heapq.heappush(myheap, st[i])

while(m):

    m-=1
    a = heapq.heappop(myheap)
    b = heapq.heappop(myheap)
    a, b = a+b, a+b
    heapq.heappush(myheap, a)
    heapq.heappush(myheap, b)

S = 0
while(len(myheap)>0):
    S += heapq.heappop(myheap)
print(S)
    

