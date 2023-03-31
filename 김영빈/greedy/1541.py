a=input().split('-')

result=0

if '+' in a[0]:
    i=a[0].split('+')
    
    for j in i:
        result+=int(j)

else :
    result+=int(a[0])


for i in a[1:]:
    if '+' in i:
        i=i.split('+')
        print(i)
        for j in i:
            result-=int(j)
    else:
        result-=int(i)
print(result)
