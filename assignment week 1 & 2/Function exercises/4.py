'4'
def opp(a):
    c=0
    a=list(a)
    for i in a:
        if i.isupper():c+=1
    print('upper:%d and lower:%d' %(c,len(a)-c))






opp(input())