#s="helloworld"
#for letter in s:
 #   print(letter,end="")

#i=0
#s1="abcd"
#s2="pqrstu"
#res=''
#if len(s1)<len(s2):
 #   spaces_to_add=len(s2)-len(s1)
  #  i=0
   # while i<spaces_to_add:
    #    s1+=' '
     #   i+=1
#elif len(s2)<len(s1):
 #   spaces_to_add=len(s1)-len(s2)
  #  i=0
   # while i<spaces_to_add:
    #    s2+=' '
     #   i+=1
#i=0
#for c1 in s1:
 #   if c1!='  ':
  #      res+=c1
   # if s2[i]!='  ':
    #    res+=s2[i]
    #i+=1
#print(res)


#i=0
#s1="abcdef"
#s2="pqrs  "
#res=''
#for c1 in s1:
 #   res+=c1+s2[i]
  #  i+=1
#print(res)


i=0
s1="abcd"
s2="pq"
res=''
big,small=(s1,s2) if len(s1)>len(s2) else(s2,s1)
for i in range(len(small)):
    res+=s1[i]+s2[i]
#print(res)
#print(i)
res+=big[i+1:] 
print(res)


#i=0
#s1="abcd"
#s2="pq"
#res=''
#big,small=(s1,s2) if len(s1)>len(s2) else(s2,s1)
#for i in range(len(small)):
 #   res+=s1[i]+s2[i]
#print(res)
#print(i)
#for j in range(i+1,len(big)):
 #   res+=big[j]
#print(res)