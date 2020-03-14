''
a=sorted(list(map(int,input().split())))
b=[]
for i in a:
    if a.count(i)==2:
        b.append(i)


for i in a:
    if i not in b:
        print(i,end=' ')
