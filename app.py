from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bestill" , methods=["GET", "POST"])
def bestill():
    if request.method == "POST":
        produkt1 = request.form["produkt1num"]
        if produkt1 == None or produkt1 == "":
            produkt1 = "0"
        produkt2 = request.form["produkt2num"]
        if produkt2 == None or produkt2 == "":
            produkt2 = "0"
        produkt3 = request.form["produkt3num"]
        if produkt3 == None or produkt3 == "":
            produkt3 = "0"
        produkt4 = request.form["produkt4num"]
        if produkt4 == None or produkt4 == "":
            produkt4 = "0"
        
        return render_template("bestillresultat.html",
                               produkt1=produkt1,
                               produkt2=produkt2,
                               produkt3=produkt3,
                               produkt4=produkt4)
    return render_template("bestill.html")


if __name__ == "__main__":
    app.run(debug=True)