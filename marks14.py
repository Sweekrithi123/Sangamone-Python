from flask import Flask,render_template
mark14=Flask(__name__)
@mark14.route("/",methods=["GET","POST"])
def Gold():
    subject1=[]
    subject2=[]
    subject3=[]
    subject4=[]
    subject5=[]
    names=[]
    names1=[]
    toppersub1=[]
    toppersub2=[]
    toppersub3=[]
    toppersub4=[]
    toppersub5=[]
    topper=[]
    total1=[]
    file1=open("marks.txt","r")
    for info1 in file1:
        list1=info1.split(",")
        print(list1)

        english=list1[3]
        mark1=english.split(":")
        for marks in mark1:
            english1=marks.split(",")

        maths=list1[4]
        mark2=maths.split(":")
        for marks in mark2:
            maths1=marks.split(",")

        physics=list1[5]
        mark3=physics.split(":")
        for marks in mark3:
            physics1=marks.split(",")

        chemistry=list1[6]
        mark4=chemistry.split(":")
        for marks in mark4:
            chemistry1=marks.split(",")

        biology=list1[7]
        mark5=biology.split(":")
        for marks in mark5:
            biology1=marks.split(",")


        for i in range(int(marks)):
            highest1=max(english1)
            highest2=max(maths1)
            highest3=max(physics1)
            highest4=max(chemistry1)
            highest5=max(biology1)
        print(highest1)
        print(highest2)
        print(highest3)
        print(highest4)
        print(highest5)

        
        total=int(highest1)+int(highest2)+int(highest3)+int(highest4)+int(highest5)
        print("Total marks of all subject is:",total)

        
        total1.append(total)
        
        
        names.append(list1[0])
        english=list1[3]
        temp=english.split(":")
        subject1.append(int(temp[1]))

        maths=list1[4]
        temp=maths.split(":")
        subject2.append(int(temp[1]))

        physics=list1[5]
        temp=physics.split(":")
        subject3.append(int(temp[1]))

        chemistry=list1[6]
        temp=chemistry.split(":")
        subject4.append(int(temp[1]))

        biology=list1[7]
        temp=biology.split(":")
        subject5.append(int(temp[1]))
    print("\n")
    print(names)
    print("\n")
        
    print(subject1)
    print(max(subject1),"is the highest marks in English")

    maxsub1=max(subject1)
    for i in range(0,26,1):
        if(subject1[i]==maxsub1):
            toppersub1.append(names[i])
    print("toppers in english is:",toppersub1)
    print("\n")

        
    print(subject2)
    print(max(subject2),"is the highest marks in Maths")

    maxsub2=max(subject2)
    for i in range(0,26,1):
        if(subject2[i]==maxsub2):
            toppersub2.append(names[i])
    print("toppers in maths is:",toppersub2)
    print("\n")

        
    print(subject3)
    print(max(subject3),"is the highest marks in Physics")

    maxsub3=max(subject3)
    for i in range(0,26,1):
        if(subject3[i]==maxsub3):
            toppersub3.append(names[i])
    print("toppers in physics is:",toppersub3)
    print("\n")

        

    print(subject4)
    print(max(subject4),"is the highest marks in Chemistry")


    maxsub4=max(subject4)
    for i in range(0,26,1):
        if(subject4[i]==maxsub4):
            toppersub4.append(names[i])
    print("toppers in chemistry is:",toppersub4)
    print("\n")

        
    print(subject5)
    print(max(subject5),"is the highest marks in Biology")

    maxsub5=max(subject5)
    for i in range(0,26,1):
        if(subject5[i]==maxsub5):
            toppersub5.append(names[i])
    print("toppers in biology is:",toppersub5)
    print("\n")


    print(total1)
    maxtotal=max(total1)
    print("overall topper score is:",maxtotal)

    maxtotal=max(total1)
    for i in range(0,26,1):
        if(total1[i]==maxtotal):
            topper.append(names[i])
    print("Overall toppers is:",topper)
    print("\n")

    return render_template("marks.html",message1=maxtotal,message2=topper,message3=toppersub1,message4=toppersub2,message5=toppersub3,message6=toppersub4,message7=toppersub5,message8=maxsub1,message9=maxsub2,message10=maxsub3,message11=maxsub4,message12=maxsub5)
if __name__=="__main__":
    mark14.run(debug=True)

