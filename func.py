#def greet(name,toSay):
 #   print(toSay,name)
#greet()
#greet("Shivani","Hi")
#print("Outside")
#for i in range(10):
 #   greet("Jinni","Annyoeng")
#greet(2001,"Hello")



#def greet(name:str):#(name:str):
 #   print("Hello"+name)
#greet()
#greet("Shivani")
#print("Outside")
#for i in range(10):
 #   greet("Jinni")
#greet(2001)
#greet([2.5,3.5])

#def addDigits(s):
 #   total=0
  #  for letter in s:
   #     if '0'<=letter<='9':
    #        total+=int(letter)
    #print(total)

#addDigits("ab12c3d5")
#words=('a2b3','7p9q','334pqr5','st5u9','abcd')
#for w in words:
 #   addDigits(w)


#def carpenter(name,money):
 #   print(f"I made a {name},I took {money} rupees")
#carpenter('chair',200)
#carpenter('table',1000)
#carpenter('chair',1000)


#x=30
#def inc():
 #   global x 
  #  x+=10
   # print('Inside',x)
    #inc(100)
#inc()                   #inc(30)----
#print('Outside',x)


#def inc(x):
 #   x+=10
  #  return x
#inc(10)
#a=20
#x=inc(a)
#print(x)


def isContanminated(ph):
    return ph<6 or ph>8
phValue=float(input("Enter ph value \n"))
print("Contminated" if isContanminated(phValue) else "Not Contaminated")
res=isContanminated(10)
print(res)