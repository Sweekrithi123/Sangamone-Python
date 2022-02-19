from flask import Flask,render_template
sort7=Flask(__name__)
@sort7.route("/",methods=["GET","POST"])

def unique():
    file1=open("a.txt","r",encoding="utf8")
    file2=open("b.txt","r",encoding="utf8")
    file3=open("sorted_a.txt","w")
    file4=open("sorted_b.txt","w")

    info1=file1.readline()
    info2=file2.readline()
        
    word1 = info1.split()
    set1=set(word1);
    word2=list(word1)
    word2.sort()
    
        
    word3 = info2.split()
    set2=set(word3);
    word4=list(word3)
    word4.sort()
         
    for word in (word1,word3):
        print(str(word))
        file3.write(str(word))
        file4.write(str(word))
        file3.write("\n")
        file4.write("\n")
    file3.close()
    file4.close()
    return render_template("Unique.html",message1=word)
if __name__=="__main__":
    sort7.run(debug=True)







