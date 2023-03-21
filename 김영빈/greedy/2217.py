n=int(input())
arr= [ list(map(int,input().split()))) for i in range(n)]

arr.sort(reverse=True)

result=[]
for i in range(n):
    result.append(arr[i]*(i+1))

print(max(arr))