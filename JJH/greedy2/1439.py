from sys import stdin
from operator import itemgetter
input = stdin.readline
str = input().rstrip('\n')

zero = 0
zero_range = 0

one = 0
one_range = 0

st = []
start = end = 0
flag = 0

for i in range(len(str)):
    
    if(str[i]=='0'):
        zero +=1
        if(flag==1): # flag 
            st.append([[start, end],end-start+1])
            one_range+=1
            start = i
        end = i
        flag = 2
    else:
        one +=1
        if(flag==2): # 
            st.append([[start, end],end-start+1])
            zero_range+=1
            start = i
        end = i
        flag = 1

if(str[start]=='0'):
    zero_range+=1
else:
    one_range+=1
st.append([[start,end],end-start+1])
# st.sort(key=itemgetter(1), reverse=True)
print(min(one_range,zero_range))
# while(st):
#     tmp = st.pop()
#     if(str[tmp[0][0]]=='0'):
#         if(zero>one):

#         else:
#     else: # 1 
#         if(zero<one):




