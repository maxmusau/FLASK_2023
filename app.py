from flask import  *
# create the app
app=Flask(__name__)
@app.route("/")
def Home():
    return render_template("index.html")
users=[] #empty list
@app.route("/signup",methods=['GET','POST'])
def Signup():
    if request.method == 'POST':
        # TODO
        # the body of if
        # get the data from the form
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        confirm=request.form['confirm_password']
        
        # input validation
        if password != confirm:
            return render_template("signup.html",message="Password does not match confirm password")
        # save the user into users list
        user={
            "username":username,
            "email":email,
            "password":password
        }
        # append the user to the users list
        users.append(user)
        print(users)
        return render_template("signup.html",message="User saved successfully")
    else:
        return render_template("signup.html")

# route to display users
@app.route("/users")  
def Users():
    return users


# import pymysql
import pymysql #connect to the database
@app.route("/employees",methods=['GET','POST'] )
def Employees():
    if request.method == 'POST':
        # TODO
        pass
    else:
        return render_template("employees.html")
           
         
    





app.run(debug=True,port=8800)