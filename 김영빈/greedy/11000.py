# 저번에 푼거랑 비슷해서 응용해보려했는데 remove말고는 방법이 안떠올라서
# 저렇게 했더니 시간초과가 나네요
N=int(input())

room=[list(map(int,input().split())) for i in range(N)]

room.sort(key=lambda x : x[0])
room.sort(key=lambda x : x[1])

# print(room)
#  강의실 개수



cnt=0

while room:
    end=0
    
    for i,j in room:
        # print(i,j)
        if i>=end:
            
            end=j

            room.remove([i,j])
            # print(room)
    cnt+=1

print(cnt)

