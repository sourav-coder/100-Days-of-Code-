''
s='google.com'
s=list(s)
import operator
d={}
#print(s)
for i  in s:
    if i in d:d[i]+=1
    else:d[i]=1

b=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print(dict(b))


