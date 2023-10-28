i=0
s1="abcd"
s2="pq"
res=''
big, small=(s1,s2) if len(s1)>len(s2) else (s2,s1)
while i<len(small):
    res+=s1[i]+s2[i]
    i+=1
res+=big[i+1:] #if i+1<len(big) else ''
print(res)