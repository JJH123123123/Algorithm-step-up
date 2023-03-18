from sys import stdin
import heapq
input = stdin.readline

n = int(input())

schedule = []

for _ in range(n):
    s, e = map(int,input().split())

    schedule.append([s,e])

schedule.sort()
pq = [] 
heapq.heappush(pq, schedule[0][1])

for i in range(1,n):
    s, e = schedule[i]
    if (pq[0] > s):
        heapq.heappush(pq, e)
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, e)
print(len(pq))

