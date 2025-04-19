from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("login.html")

@app.route("/insertuser")
def insert():

    return render_template("insert.html")

@app.route("/userdelete")
def delete():

    return render_template("deleteuser.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="777")
