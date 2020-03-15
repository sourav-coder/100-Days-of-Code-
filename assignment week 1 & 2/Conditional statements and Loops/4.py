'4'
for i in range(100,400):
    s=list(str(i))
    c=0
    for j in s:
        if int(j)&1==0:c+=1
    if c==3:print(int(i),end=',')