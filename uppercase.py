#res=''
#name=input("Enter your name")
#i=0
#while i<len(name):
 #  letter=name[i]
  # value=ord(letter)
   #print(value)    
   #res+= chr(value-32) if 'a'<=letter<='z' else letter
   #i+=1
#print(res)  
 
from string import ascii_lowercase,ascii_uppercase
res=''
name=input("Enter your name ")
i=0
while i<len(name):
    letter=name[i]
    if 'a'<= letter <='z':
        j=0
        while ascii_lowercase[j]!=letter:
            j+=1
        letter=ascii_uppercase[j]
    res+= letter
    i+=1
print(res)
