'7'
a=[(10,20,30),(40,50,60),(70,80,90)]


b=[]
for i in a:

    t=list(i)
    t[2]=100

    b.append(tuple(t))



print(b)
