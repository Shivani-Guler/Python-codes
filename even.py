num=int(input("Enter a num"))
end=int(input("Enter end num"))
#i=num
#while i<end:
 #   if i%2==0:
  #      print(i)
#i+=1

i=(num+1) if num%2 else num
while i<end:
    print(i)
    i+=2
 