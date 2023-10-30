#---------------fact-----
def factorial(n):
	
	res = 1
	
	for i in range(2, n+1):
		res *= i
	return res

num = 5
print("Factorial of", num, "is",factorial(num))


#-------------fib-------

# def fib (n): 
#     if( n == 0):
#         return 0
#     else:
#         x = 0
#         y = 1
#         for i in range(1,n):
#             z = (x + y)
#             x = y
#             y = z
#             return y

# for i in range(10):
#     print (fib(i))



 