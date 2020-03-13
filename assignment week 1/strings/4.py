''
l=input()
l=l.split(' ')
d={l[i]:l.count(l[i]) for i in range(0,len(l),2)}
print(d)