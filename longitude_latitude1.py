from flask import Flask,render_template
longitude_latitude1=Flask(__name__)
@longitude_latitude1.route("/",methods=["GET","POST"])
def lat_lon():
    from math import sqrt
    x1=float(input("enter the 1st latitude value:"))
    y1=float(input("enter the 1st longitude value:"))
    x2=float(input("enter the 2nd latitude value:"))
    y2=float(input("enter the 2nd longitude value:"))

    distance= sqrt((y2-y1)*(y2-y1)*  + (x2-x1)*(x2-x1))
    print("Distance is:",distance)
    return render_template("distance.html",message1=distance)
if __name__=="__main__":
    longitude_latitude1.run(debug=True)

