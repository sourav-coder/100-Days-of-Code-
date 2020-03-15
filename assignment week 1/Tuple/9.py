'9'
a=[('item1','12.20'),('item2','15.10'),('item3','24.5')]
a.sort(key=lambda x:float(x[1]),reverse=True)
print(a)