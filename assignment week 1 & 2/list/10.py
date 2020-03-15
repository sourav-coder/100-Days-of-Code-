'10'
a=list(map(str,input().split()))
a=''.join(a)
a=a.split(',')
print(a)
f=0
for i in a:
    if i!='{}':
        f=1

if f==0:print('True')
else:print('False')