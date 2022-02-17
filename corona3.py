list1=[]
list2=[]

file1=open("WHO_data.csv","r")
for i in range(0,25,1):
    
    info1=file1.readline().replace("\n","").replace("Deaths - cumulative_total","").replace("Name","").split(",")
    print(info1)
    list1.append(info1[3])
    list2.append(info1[0])
print()
print(list1)
print()
print(list2)

for i in range(len(list1)):
    print(list1[i])
    print(list2[i])
print(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9],list1[10])
print(list2[0],list2[1],list2[2],list2[3],list2[4],list2[5],list2[6],list2[7],list2[8],list2[9],list2[10])
