from flask import  *
import pymysql #connect to the database
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

connection=pymysql.connect(host="localhost",user="root",database="alpha",password="")
# import pymysql

@app.route("/employees",methods=['GET','POST'] )
def Employees():
    if request.method == 'POST':
        # TODO
        emp_name=request.form['emp_name']
        salary=request.form['salary']
        dept_id=request.form['dept_id']
        # check if user has provided all the details
        if not emp_name or not salary or not dept_id:
            return render_template("employees.html",message="Please fill in all the details")
        # create the cursor function
        # cursor function -used to execute the sql query
        cursor=connection.cursor()
        # define the sql
        sql='insert into employees (emp_name,salary,dept_id) values(%s,%s,%s)' 
        # execute sql
        cursor.execute(sql,(emp_name,salary,dept_id))
        # commit
        connection.commit()
        # return statement
        return render_template("employees.html",message="Employee saved successfully")
        # pass
    else:
        return render_template("employees.html")
           
         
# check database connection    # 
@app.route("/check_database")
def Check_database():
    try:   
        connection=pymysql.connect(host="localhost",user="root",database="alpha",password="")
        print("Connection successful")
        return "Connection successful"
    except:
        return "Connection failed"





app.run(debug=True,port=8800)