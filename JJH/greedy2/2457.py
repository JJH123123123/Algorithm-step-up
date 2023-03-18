from sys import stdin
from functools import cmp_to_key
from collections import deque

input = stdin.readline

n = int(input())

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
         # 0, 1, 2, 3, 4,     5,  6,  7, 8,  9,  10, 11, 12

months_prefix = [0]*len(months)
months_prefix[0] = months[0]
for i in range(1, len(months)):
    months_prefix[i] = months_prefix[i-1] + months[i]
# st = [] 

def cmp(a, b): # a = [1,2,3,4] 01.02 - 03.04
    A = months_prefix[a[2]-1] + a[3]  - months_prefix[a[0]-1] + a[1] 
    # 기간 
    B = months_prefix[b[2]-1] + b[3]  - months_prefix[b[0]-1] + b[1] 
    # 시작 기간 먼저 
    if (a[0]==b[0]):
        if(a[1]==b[1]):
            if( A > B ):
                return -1
            elif A == B:
                return 0 
            else:
                return 1 
        else: # 
            if(a[1]>b[1]):
                return 1
            else:
                return -1  
    else:# 다르다면 ? 
        if(a[0]>b[0]):
            return 1 
        else:
            return -1 
        


# 1. 3.1 - 11.30까지 매일 꽃 하나 
# 2. 정원에 심는 꽃 가능한 적게 
st = []
for _ in range(n):
    st.append(list(map(int,input().split())))

st.sort(key=cmp_to_key(cmp))


Dates = [st[0]]
Size = 1

for i in range(n):
    if(Dates[-1][:2]==st[i][:2]):continue
    Dates.append(st[i])
    Size+=1



tmp = [3,1]
end = [11,30]
possible = [0, 0 ]
cnt = 0
idx = 0
flag = False

# end check for 11/30 if not return 0 
# 1 2 3 4 
while(tmp[0]*100 + tmp[1] <= 1130):
    for i in range(idx, Size):
        if(tmp[0] * 100 + tmp[1] < Dates[i][0] * 100 + Dates[i][1]):
            break
        if(possible[0] * 100 + possible[1] < Dates[i][2] * 100 + Dates[i][3]):
            possible = Dates[i][2:] # end time 
            idx = i
    if(tmp == possible):
        flag = True
        break
    else:
        cnt+=1
        tmp = possible

if(flag):
    print(0)
else:
    print(cnt)
# 시작 빠른, 동시에 끝나는 게 더 느린 것 순서대로 
# 
# 정렬 

# 포문 
# 
# 출력 