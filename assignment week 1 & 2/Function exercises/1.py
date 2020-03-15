'1'
def large(a,b,c):
    if a>b and a>c:print(a)
    elif b>a and b>c:print(b)
    else:print(c)


a,b,c=map(int,input().split())
large(a,b,c)
