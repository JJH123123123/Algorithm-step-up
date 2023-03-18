
n = int(input())
st1 = list(map(int,input().split()))
st1.sort()
st2 = list(map(int,input().split()))
st2.sort(reverse=True)

S = 0
for i in range(n):
	S += st1[i] * st2[i]

print(S)	


