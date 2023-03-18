from sys import stdin
input = stdin.readline

tmp = [] 
arr = []
n = int(input())
def merge(start, mid, end):
    global n
    i = start
    j = mid + 1 
    k = start
    while( i<= mid and j<=end):
        if(arr[i] < arr[j]):
            tmp[k] = arr[i]
            i+=1
        else:
            tmp[k] = arr[j]
            j+=1
        k+=1

    if(i<=mid):
        while(i<=mid):
            tmp[k] = arr[i]
            k+=1
            i+=1
    else:
        while(j<=end ):
            tmp[k] = arr[j]
            k+=1
            j+=1

    for l in range(start, end+1):
        arr[l] = tmp[l]
    return 

def mergeSort(start, end):
    if(start<end):
        mid = (start+end)//2
        mergeSort(start, mid)
        mergeSort(mid+1, end)
        merge(start,mid, end)
    return 
    


arr = list(map(int,input().split()))
tmp = [0]*(n)

mergeSort(0,n-1)
time = 0
cnt = 0
for i in range(n):
    time += arr[i]
    cnt += time
print(cnt)
