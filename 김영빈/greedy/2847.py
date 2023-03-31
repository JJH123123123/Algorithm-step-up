N=int(input())

num=[int(input()) for i in range(N)]
# 총 카운트
cnt=0
while 1:
    # 한 사이클 카운트
    new_cnt=0
    for i in range(N-1):
        while 1:
            if num[i]>=num[i+1]:
                num[i]-=1
                new_cnt+=1
            else:
                break
    cnt+=new_cnt
    if new_cnt ==0:
        break;
print(cnt)
