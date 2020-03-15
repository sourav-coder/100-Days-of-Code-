'4'
a=list(map(int,input().split()))
b=list(map(int,input().split()))

d=[]
for i in range(len(a)):
    if a[i]>b[i]:
        d.append(a[i]-b[i])
    else:d.append(b[i]-a[i])
print(d)