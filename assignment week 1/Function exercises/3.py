'3'

def mul(a):
    s=1
    for i in a:s*=i
    print(s)



mul(list(map(int,input().split())))