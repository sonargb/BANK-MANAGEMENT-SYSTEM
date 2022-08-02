
from flask import request as req
from flask import Flask, render_template, redirect, url_for
import database as db
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/customerlist")
def customerlist():
    clist = db.all()
    return render_template("customerlist.html", clist=clist)


@app.route("/customerdelete/<int:AccountNumber>")
def accClose(AccountNumber):
    db.clsac(AccountNumber)
    return redirect(url_for("customerlist"))


@app.route("/addaccount", methods=["GET", "POST"])
def addaccount():
    if req.method == "GET":
        return render_template("addaccount.html")
    elif req.method == "POST":
        name = req.form["CustomerName"]
        num = req.form["AccountNumber"]
        dob = req.form["DateOfBirth"]
        cont = req.form["Contact"]
        addr = req.form["Address"]
        b = req.form["Balance"]
        db.openAc(CustomerName=name, AccountNumber=num,
                  DateOfBirth=dob, Contact=cont, Address=addr, Balance=b)
        return redirect(url_for("customerlist"))


@app.route("/updateaccount/<int:AccountNumber>", methods=["GET", "POST"])
def updateaccount(AccountNumber):
    if req.method == "GET":
        customer = db.display(AccountNumber)
        return render_template("updateaccount.html", customer=customer)
    elif req.method == "POST":
        name = req.form["CustomerName"]
        dob = req.form["DateOfBirth"]
        cont = req.form["Contact"]
        addr = req.form["Address"]
        b = req.form["Balance"]
        db.update(CustomerName=name, DateOfBirth=dob, Contact=cont,
                  Address=addr, Balance=b, AccountNumber=AccountNumber)
        return redirect(url_for("customerlist"))


@app.route("/depositeamount", methods=["GET", "POST"])
def depositeamount():
    if req.method == "GET":
        return render_template("depositeamount.html")
    elif req.method == "POST":
        num = req.form["AccountNumber"]
        am = int(req.form["DepositeAmount"])
        db.depam(am, num)
        return "<h1>Amount Deposited Successfully.</h1>"


@app.route("/withdrawamount", methods=["GET", "POST"])
def withdrawamount():
    w = 1
    if req.method == "GET":
        return render_template("withdrawamount.html")
    elif req.method == "POST":
        num = req.form["AccountNumber"]
        am = int(req.form["WithdrawAmount"])
        w = db.widram(am, num)
        if w == 0:
            msg="Insufficient balance"
        else:
            msg = "Amount Withdrawn Successfully"
        clist = db.all()
        return render_template("customerlist.html", clist=clist,msg=msg)
@app.route("/aboutus")
def aboutus():
    return render_template("about.html")


@app.route("/searchResult", methods=["GET", "POST"])
def searchResult():
    if req.method == "GET":
        return("index.html")
    elif req.method == "POST":
        searchName = req.form["CustomerName"]
        res = db.displayAccount(searchName)
        return f'''<h2>Name: {res[0]}
        <br>Account Number: {res[1]}
        <br>DOB: {res[2]}
        <br>Mobile: {res[3]}
        <br>Address: {res[4]}
        <br>Balance: {res[5]}</h2>'''


if __name__ == "__main__":
    app.run(debug=True)
