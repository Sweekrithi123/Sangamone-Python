count=100
doors=[False]*(count)
for j in range(0,count,1):
    for i in range(j,count,j+1):
        doors[i]=not doors[i]

free=[i+1 for i in range(0,count) if doors[i]==True]
print("lucky prisoners are:",free)
