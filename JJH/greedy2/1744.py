from sys import stdin
input = stdin.readline

n = int(input())

posi = []
minus = []
for _ in range(n):
    tmp = int(input())
    if(tmp>0):
        posi.append(tmp)
    else:
        minus.append(tmp)

posi.sort(reverse=True)
S = 0
posi_size = len(posi)

for i in range(0,posi_size,2):
    tmp = posi[i]
    if(i!=posi_size-1):
        tmp *= posi[i+1]
        tmp_sum = posi[i+1]+posi[i]
        if(tmp> tmp_sum):
            S += tmp
        else:
            S += tmp_sum
    else:
        S += tmp

nega_size = len(minus)
minus.sort()
M = 0
for i in range(0,nega_size,2):
    tmp = minus[i]
    if(i!=nega_size-1):
        tmp *= minus[i+1]
        M += tmp
    else:
        M += tmp        
print(S + M)




