# def foo():
#     print("Foo Foo")

# def bar():
#     print("Bar Bar")

# def caller(f):
#     f()

# caller(foo)
# caller(bar)


# def foo(**kwargs):
#     print(kwargs)
# foo(sep='\n', end='\t', name='_')

#---------------------------------------------

# def squareV1(nos):
#     return [e**2 for e in nos]   #--list comprehension--
# nos=[3,2,8,7]
# print(squareV1(nos))


# def squareV1(nos):
#     res=[]
#     for e in nos:
#         res.append(e**2)
#     return res
# nos=[3,2,8,7]
# print(squareV1(nos))

# ----------------------------------------

# nos=[3,2,8,7]
# res=map(lambda x:x**2,nos)
# # for e in res:
# #     print(e)
# #print(res)
# e=next(res)
# print(e)
# e=next(res)  
# print(e)

#---------------------------------------------------

def square(nos):
    return (e**2 for e in nos) #generator comprehension
    # for e in nos:
    #     yield e**2
nos=[3,2,8,7]
res=square(nos)
#print(res)
e=next(res)
print(e)