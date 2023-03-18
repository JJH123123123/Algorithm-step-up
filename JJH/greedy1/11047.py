from sys import stdin
input = stdin.readline

n, m = map(int, input().split())


st = [] 
for _ in range(n):
	st.append(int(input()))

st.sort(reverse=True)

cnt = 0
for i in range(n):
	if(m<st[i]):
		continue	
	q = m//st[i]
	m -= q * st[i]
	cnt += q
print(cnt)
		
