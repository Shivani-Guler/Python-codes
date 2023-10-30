#str = input("Enter the name:")
#i = 0
#ch2 = ''

#while str[i:]:
    #ch = ord(str[i])
    #if ch > 64 and ch < 91:
    #    ch2 += chr(ch+32)
    #else:
     #   ch2 += chr(ch)
    #i += 1
#print("Res", ch2)

from string import ascii_lowercase,ascii_uppercase
res=''
name=input("Enter your name ")  
i=0
while i<len(name):
    letter=name[i]
    if 'A'<= letter <='Z':
        j=0
        while ascii_uppercase[j]!=letter:
            j+=1
        letter=ascii_lowercase[j]
    res+= letter
    i+=1
print(res)