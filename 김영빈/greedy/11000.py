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