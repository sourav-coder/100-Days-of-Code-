'4'
t=(1,2,3,2,3)
t1=()
for i in set(t):
    if t.count(i)>1:
        t1+=i,

print(t1)
