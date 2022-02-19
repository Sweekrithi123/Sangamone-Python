from flask import Flask,render_template
image1=Flask(__name__)
@image1.route("/",methods=["GET","POST"])
def image():
    with open("img4.png",'rb') as img_file:
        img_file.seek(163)
        a = img_file.read(2)
        height = (a[0] << 8) + a[1]
        a = img_file.read(2)
        width = (a[0] << 8) + a[1]
        print("The resolution of the image is",width,"x",height)
        return render_template("image.html",message1=(width,"x",height))
if __name__=="__main__":
    image1.run(debug=True)


