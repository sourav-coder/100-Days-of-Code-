'6'
t=(1,2,3)
d={}
for i in t:
    if i  not in d:d[i]=1
    else:d[i]+=1
print(d)