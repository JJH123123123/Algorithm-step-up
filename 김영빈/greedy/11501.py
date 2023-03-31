t=int(input())

for i in range(t):
    
    n=int(input())
    arr=list(map(int,input().split()))

    arr=arr[::-1]

    M=arr[0]
    cnt=0
    for j in range(n):
        
        if arr[j]>M:
            M=arr[j]
        else:
            cnt+=M-arr[j]

    print(cnt)