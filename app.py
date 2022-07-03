import sqlite3
from flask import Flask, redirect, render_template,request
app= Flask(__name__)

@app.route("/")
def index():
    """Show portfolio of stocks"""
    return render_template("index.html")


@app.route('/login' , methods=['GET','POST'])

def login():
   if request.method=='POST':

       connection = sqlite3.connect("user.db")
       cursor = connection.cursor()

       name=request.form("username")
       
       password=request.form("password")

       query ="SELECT * FROM users WHERE (Name,Password)  VALUES(?,?)", (name, password)

       cursor.execute(query)

       result = cursor.fetchall()

       if len(result)==0:
            print("somthing went wrong")

       else:
            return render_template('/')

   else: 
     return redirect('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":

        # Ensure username was submitted
        return render_template("register.html")

    else:
         connection = sqlite3.connect("user.db")
         cursor = connection.cursor()

         username= request.form.get("username")
         password= request.form.get("password")
         reenter = request.form.get("reenter")

         if not username:
             return ("Enter Username")
         if not password:
             return ("Enter passwoed")
         if not reenter:
             return("retype password")
         if password  != reenter :
              return("Passwords did not match")

        
    new_user= "INSERT INTO users (Name,Password) VALUES (?,?)" , (username, password)
    cursor.execute(new_user)    
    connection.cursor()
    cursor.commit()
    return render_template("login.html")