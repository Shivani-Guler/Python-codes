# nos=[10,20,30,[200,300]]
# def inc(d):
    
#     d[-1][0]+=20
#     print("Inside",d)
# inc(nos[:])                            #shallow copy
# print("outside",nos)



# nos=[10,20,30]
# def inc(d):
#     d=d.copy()
#     d[0]+=20
#     print("Inside",d)
# inc(nos)
# print("outside",nos)


# nos=[10,20,30]
# def inc(d):
    
#     d[0]+=20
#     print("Inside",d)
# inc(nos[:])                            #shallow copy
# print("outside",nos)


# def add(x=10,y=10):
#     return x+y
# res=add(3,5)
# print(res)
# print(add(20))
# print(add())


def add(*vals):
    total=0
    for e in vals:
        total+=e
    return total                        

print(add(2,3,4,5))
 