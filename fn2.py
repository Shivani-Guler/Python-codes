# def makeFoo(msg):
#     def foo():
#         print("Foo Foo",msg)
#     return foo
# f=makeFoo("Jinnie")
# f()


# def makeAdder(a):
#     def add(b):
#         return a+b
#     return add
# # f=makeAdder(10)
# # print(f(20))
# res=makeAdder(50)(20) #function curry
# print(res)


def makeAdder(a):
    def add(b):
        nonlocal a
        a+=1
        return a+b
    return add
res=makeAdder(50)(20)
print(res)