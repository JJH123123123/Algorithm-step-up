from sys import stdin
input = stdin.readline

n = int(input())
st = []
for i in range(n):
    st.append(int(input()))

# st.sort()
S = 0
for i in range(n-1,0,-1):
    if(st[i-1] >= st[i]):
        tmp = (st[i-1]-st[i]+1)
        S += tmp
        st[i-1] -= tmp
# print(st)
print(S)
