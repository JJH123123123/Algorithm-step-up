from sys import stdin
input = stdin.readline

exp = list(input().strip('\n').split('-'))

st = [] 
for i in range(len(exp)):
    st.append(list(map(int,exp[i].split('+'))))

cnt = sum(st[0])
for i in range(1,len(st)):
    cnt -= sum(st[i])
print(cnt)
