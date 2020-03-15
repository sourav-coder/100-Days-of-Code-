'9'
a=list(map(str,input().split()))
b=list(map(str,input().split()))
c=[]
d=[]
for i in a:
    if i not in b:
        d.append(i)


for i in b:
    if i not in a:
        c.append(i)

print(c,d)
