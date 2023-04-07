
n, m = map(int, input().split())

nums = list(map(int,input().split()))

present = [0] * (n+1)

# 멀티탭 플러그에 있으면 빼지 않는다. 
# 다 차있다. => 하나를 빼야 한다.
# 그렇지 않다. => 빈공간이 있다. => 그냥 넣는다. 
res = 0
for i in range(m):

    flag = False

    # 빈 플러그가 존재하는 경우 
    for j in range(n):
        if(present[j]==0): 
            present[j] = nums[i]
            flag = True
            break
        
        # 같은 아이템이 플러그에 존재하는 경우 
        if(present[j] == nums[i]):
            flag = True
            break

    if(flag): continue

    # 빈 플러그도 없고, 같은 플러그도 없는 경우
    M = -1
    idx = 0
    for l in range(n): # 현재 플러그 중
        cnt = 0
        for k in range(i+1,m): # 다음 위치에 있는 아이템 중에서
            # 가장 멀리 있는 아이템을 찾아야 함. 
            if(present[l] == nums[k]):
                break
            cnt+=1 
        
        if(M < cnt): # 두개가 거리가 같다면, 어느 걸 빼도 ok 
            M = cnt
            idx = l # 바뀌는 플러그 인덱스
    
    present[idx] = nums[i]
    res+=1 
print(res)