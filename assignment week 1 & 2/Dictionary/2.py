'2'
a={'a':100,'b':200,'c':300}
b={'a':300,'b':200,'d':400}
for key in b:
    if key in a:
        a[key]+=b[key]
    elif key not in a:
        a[key]=b[key]



from collections import Counter
z=Counter(a)
print(z)