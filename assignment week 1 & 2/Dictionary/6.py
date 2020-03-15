'6'
a=[{'id':1,'success':True,'name':'Lary'},{'id':2,'success':True,'name':'Rabi'},{'id':1,'success':False,'name':'Alex'}]
d1=a[0]
d2=a[1]
d3=a[2]
c=0
for i in a:
    for key,val in i.items():
        if key=='success' and val==True:c+=1
print(c)