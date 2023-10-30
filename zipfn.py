#for c1,c2 in zip("abcd","pqrs"):
 #   print(c1,c2)

#import itertools as it
#for e in it.zip_longest("abcd","pq","mnop",fillvalue="#"):
 #   print(e)

import itertools as it
#s1="abcd"
#s2="pq"
#res=''
#for c1,c2 in it.zip_longest(s1,s2,fillvalue=''):
 #   res+=c1+c2
#print(res)


#e=('a','b','c',20,30,40,50)
#print(e)
#c1,*c2,c3=e
#print(c1,c2,c3)

#a=[1,2,3,4]
#b=[10,20,30]
#c=a+b
#print(c)
#[1, 2, 3, 4, 10, 20, 30]


num_of_strings=int(input("Enter num of strings"))
words=[]
res=''
for i in range(num_of_strings):
    s=input(f"Enter string{i+1}\n")
    words.append(s)
    #words+=[s]
#print(words)
for e in it.zip_longest(*words,fillvalue=''):
    #print(e)
    for c in e:
        res+=c
print(res)