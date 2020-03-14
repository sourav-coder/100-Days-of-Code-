'3'
d={}
n=int(input())
while n>0:
    n-=1
    print('enter key and value ')
    key,val=map(str,input().split())
    d[key]=val

#print(d)
a=set()
for i in d.values():
    if i not in a:
        a.add(i)
print(a)
