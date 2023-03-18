from sys import stdin
input = stdin.readline
        
n = int(input())

st = [] 
for _ in range(n):
    s, e = map(int, input().split())
    if(s>e):
        st.append([e,s])
    else:
        st.append([s,e])

st.sort()
s = -pow(10,10)*2#st[0][0]
e = -pow(10,10)*2#st[0][1]
cnt = 0

for i in range(n):
    if(st[i][0]>e):
        s = st[i][0]
        e = st[i][1]
        cnt += abs(e-s)
    else:
        if(e<st[i][1]):
            cnt += abs(st[i][1]-e)
            e = st[i][1]

print(cnt)








