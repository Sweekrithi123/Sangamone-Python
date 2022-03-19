def diamond2():
    
    s1="Sweekrithi"
    s2=" "
    output1=""
    len1=len(s1)

    for j in range(1,len1+1,1):   
        for i in range(0,len1-j,1):
            output1=s2+output1
        output1=output1+"\n"
        output1=output1+s1[0:j]

    for j in range(1,len1,1):   
        for i in range(0,j,1):
            output1=s2+output1
        output1=output1+"\n"
        output1=output1+s1[0:len1-j]
    return output1
result=diamond2()
print(result)
