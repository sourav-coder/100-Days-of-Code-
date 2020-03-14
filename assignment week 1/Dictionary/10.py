'10'
x={'key1':1,'key2':2,'key3':3}
y={'key1':1,'key2':3}
a=[]
for key,val in x.items():
    for k,value in y.items():
        if k==key and val==value:a.append(str(key)+':'+str(val))

for i in a:
    print(i,'is present in both x and y')