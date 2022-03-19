s1="Sweekrithi"
len1=len(s1)
s2=" "
for j in range(0,len1-5,1):   
    for i in range(0,len1-5-j,1):
        print(s2,end="")
    print(s1[0:(1+(2*j))])


for j in range(len1-7,-1,-1):   
    for i in range(0,len1-5-j,1):
        print(s2,end="")
    print(s1[0:(1+(2*j))])


