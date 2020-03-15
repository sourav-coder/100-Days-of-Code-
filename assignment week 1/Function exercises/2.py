'2'
def sum(a):
    s=0
    for i in a:s+=i
    print(s)

sum(list(map(int,input().split())))