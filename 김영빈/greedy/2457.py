from sys import stdin
N=int(stdin.readline())

arr=[list(map(int,stdin.readline().split())) for i in range(N)]

arr_sort=sorted(arr,key=lambda x: x[1])
arr_sort=sorted(arr_sort,key=lambda x: x[0])

start=arr_sort[0]
# print(arr_sort)
cnt=1
for i in arr_sort:
        if i[0]<3 or (i[0]==3 and i[1]==1):
            if i[2]>start[2]:
                start=i
            elif i[2]==start[2] and i[3]>start[3]:
                start=i

def func(start):
    
    
    fake_start=start
    for i in range(arr_sort.index(start)+1,N):
        
        # print(arr_sort[i],1)
        if (arr_sort[i][0]>start[2]) or (arr_sort[i][0]==start[2] and arr_sort[i][1]>start[3]):
            #   print(1,arr_sort[i])
              break
        else:
             
             if arr_sort[i][2]>fake_start[2] or (arr_sort[i][2]==fake_start[2] and arr_sort[i][3]>fake_start[3]):
                  fake_start=arr_sort[i]
            #   print(fake_start,arr_sort[i])   

        
    
         
    return fake_start
# start=func(start)
# print(start,2)
# start=func(start)
# print(start,3)
while 1:
    if start[2]>11 or (start[2]==11 and start[3]==31):
         break
    
    
    start=func(start)
    cnt+=1
    #11월 넘으면 끝
    # print(start)
    
    
print(cnt)





