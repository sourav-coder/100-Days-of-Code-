s=input()
c=''
for i in list(s):
    if i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='U' or i=='u':
        c+=i
c=list(c)
d={c[i]:s.count(c[i]) for i in range(0,len(c),2)}
print(d)


