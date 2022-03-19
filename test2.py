def diamondleft():
    
    s1="Sweekrithi"
    s2=" "
    len1=len(s1)
    output1=""

    for j in range(1,len1+1,1):   
        for i in range(0,len1-j,1):
            output1=output1+s2
        
        output1=output1+s1[0:j]
        output1+="\n"

    for j in range(1,len1,1):   
        for i in range(0,j,1):
            output1=output1+s2
        output1=output1+s1[0:len1-j]
        output1+="\n"
    return output1
result=diamondleft()
print(result)
