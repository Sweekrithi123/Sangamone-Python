file1=open("mail1.txt","r")
file2=open("mail2.txt","r")
info1=file2.readline().replace("\n","").split(",")
print(info1)
list1=str(info1[0])
list2=str(info1[1])
list3=str(info1[2])
list4=str(info1[3])
print(list1)
print(list2)
print(list3)
print(list4)

info2=file1.readline().replace("Freind1",list1)
print(info2)
info3=info2.replace(list1,list2)
print(info3)
info4=info3.replace(list2,list3)
print(info4)
info5=info4.replace(list3,list4)
print(info5)
