from flask import Flask,request,render_template,redirect
from flask_mysqldb import MySQL
import mysql.connector
import webbrowser


app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'foodbank'

cursor = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="foodbank"
  )
 
mysql = MySQL(app)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT * FROM donor')
            mydata=cursor.fetchall();
            return render_template("index.html",data=mydata)

    if request.method=="POST":
        name=request.form["name"];
        address=request.form["address"];
        phone=request.form["phone"];
        classes=request.form["classes"];
        name1=request.form["name1"];
        quantity1=request.form["quantity1"];
            
        cursor=mysql.connection.cursor()
        cursor.execute('''Insert INTO donor(Name,Address, Phone_Number,Food_Type,Item_Name,Quantity) Values(%s,%s,%s,%s,%s,%s)''',(name,address,phone,classes,name1,quantity1))

        mysql.connection.commit();

        return redirect("/")

@app.route("/req",methods=["GET","POST"])
def index1():
    if request.method=="GET":
            return render_template("request.html")

    if request.method=="POST":
        rname=request.form["rname"];
        mno=request.form["mno"];
        don=request.form["donation"];
        add=request.form["add"];
        needs=request.form["needs"];

        cursor=mysql.connection.cursor();
        cursor.execute('''INSERT INTO request(Name,No,Address,needs,item_Type) Values(%s,%s,%s,%s,%s)''',(rname,mno,add,needs,don))

        mysql.connection.commit();

    return redirect("/")


@app.route("/Donor",methods=["GET","POST"])
def l():
        
        if request.method=="GET":
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT * FROM donor')
            mydata=cursor.fetchall();
            return render_template("index.html",data=mydata)

        if request.method=="POST":
            
            name=request.form["name"];
            address=request.form["address"];
            phone=request.form["phone"];
            classes=request.form["classes"];
            name1=request.form["name1"];
            quantity1=request.form["quantity1"];

            rname=request.form["rname"];
            mno=request.form["mno"];
            don=request.form["dno"];
            add=request.form["add"];
            needs=request.form["needs"];
            


            
            cursor=mysql.connection.cursor();
            cursor2=mysql.connection.cursor();
            cursor.execute('''Insert INTO donor(Name,Address, Phone_Number,Food_Type,Item_Name,Quantity) Values(%s,%s,%s,%s,%s,%s)''',(name,address,phone,classes,name1,quantity1))
            cursor2.execute('''Insert INTO Request(Name,Address, No,needs,item_Type) Values(%s,%s,%s,%s,%s)''',(rname,mno,add,needs,don))

            mysql.connection.commit();

        


    
        return render_template("index.html")



@app.route("/maps")
def index3():
    return render_template('foodbank.html')

@app.route("/tips")
def index4():
    return render_template("tips.html")


    
if __name__ == '__main__':
  app.run(debug=True)