import heapq
from operator import itemgetter
from sys import stdin
input = stdin.readline

n = int(input())

nums = [list(map(int,input().split())) for _ in range(n) ]
nums.sort(key=itemgetter(0))
nums.sort(key=itemgetter(1))

pq = [pow(10,10)] 

for i in range(n):
    if(pq[0]<=nums[i][0]):
        heapq.heappop(pq)
        heapq.heappush(pq, nums[i][1])
    else:
        heapq.heappush(pq, nums[i][1])

print(len(pq)-1)