''
l=input()
l=l.split(' ')
c=0
for i in l:
    c=max(len(i),c)
print(c)