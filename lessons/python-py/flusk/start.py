from flask import Flask, render_template 
from flask import jsonify, url_for, redirect, request

app = Flask(__name__)

title = "bashtalgych bet"

db = [

    {
        "name": "Azatik",
        "school": "Rock Creek",
        "age": 10
    
    },

    {
        "name": "Beka",
        "school": "stoller",
        "age": 13
    }
]

a=1
if a == 1:
    db[0]["name"] = "Sezim"
    db[0]["school"] = 'kindergarten'
    db[0]['age'] = 5




@app.route("/", methods=["POST", "GET"])
def main():
    return redirect(url_for("home"))


@app.route("/home", methods=["POST", "GET"])
def home():
    val = None
    if request.method == "POST":
        if request.form.get("name"):
            val = request.form['name']

    return render_template("./index.html", title=title, db=db, val=val )

@app.route("/info", methods=["POST", "GET"])
def info():
    return render_template("./mirlan-Z97X-UD7-TH.html")




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)





