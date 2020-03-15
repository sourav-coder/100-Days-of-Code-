'1'
e=0
a=list(map(int,input().split()))
for i in a:
    if i&1==0:e+=1
print('even:%d and odd:%d'%(e ,len(a)-e))