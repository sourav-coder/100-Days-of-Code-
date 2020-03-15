'10'
a=[1,2,3,(1,2),(3,4),5,6]
c=0
for i in a:
    if isinstance(i,tuple):break
    c+=1
print(c)