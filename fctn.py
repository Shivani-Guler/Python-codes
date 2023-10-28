def add(x,y):
    return x+y

def mul(a,b):
    return a*b

#y=mul(8,5)
#z=mul(5,9)
#p=mul(z,20)
#q=add(2,y)
#res=add(q,p)
res=add(2,add(mul(8,5),mul(mul(5,9),20)))
print(res)