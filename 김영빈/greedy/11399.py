n=int(input())

p=list(map(int,input().split()))
ans=0
p.sort()

for i in p:
    ans+=i*n
    n-=1
    
print(ans)