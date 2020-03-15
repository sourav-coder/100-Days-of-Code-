'8'
#sample data
a={'1':['a','de','bv'],'2':['d','ab']}
for key,val in a.items():
    a[key]=sorted(val)
print(a)
