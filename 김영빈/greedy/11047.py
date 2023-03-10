n,k=map(int,input().split())

arr=[int(input()) for coins in range(n)]
result=0
arr.sort(reverse=True)

# while 없어도 됨
while k!=0:
    for i in arr:
        if k>=i:
            result+=k//i
            k=k%i
print(result)
