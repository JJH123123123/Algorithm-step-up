from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * (n+1)
ans = 0
nums = list(map(int,input().split()))
for i in range(n):
	x = nums[i]
	dp[x] = dp[x-1] + 1
	ans = max(dp[x],ans)

print(n-ans)	
