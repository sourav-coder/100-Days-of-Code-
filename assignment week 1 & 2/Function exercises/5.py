'5'
def even(a):
    for i in a:
        if i&1==0:print(i)




even(list(map(int,input().split())))