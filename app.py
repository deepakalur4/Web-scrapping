from flask import Flask,redirect,render_template,url_for,request
import scrap
#WSGI
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/results",methods=["POST","GET"])
def results():
    if request.method=="POST":
        its=scrap.my_func(request.form["Job name"])
        return its
        

if __name__=="__main__":
    app.run(debug=True)