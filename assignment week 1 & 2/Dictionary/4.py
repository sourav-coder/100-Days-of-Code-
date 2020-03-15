'4'
d={}
s=''
n=int(input())
while n>0:
    n-=1
    print('enter key and value ')
    key=input()
    val=list(map(str,input().split()))
    d[key]=''.join(val)
    s+=''.join(val)

#print(d)
a=[]
for val in d.values():
    a.append((val))
#print(a)
from itertools import combinations
l=len(a)
b=set(combinations(s,l))
#print(b)
c=[]
for i in b:
    c.append(''.join(i))
#print(c)
for i in c:
    if i in a:
        c.remove(i)
print(c)

