# Flask module
# import flask
from flask import Flask,jsonify,render_template
# create the application
app=Flask(__name__)
# crete the main route
@app.route("/")
# function for the main route
def main():
    # TODO
    return "This is the Main Route"

# create two more routes and return some string text
@app.route("/about")
def about():
    return "This is the about page"

# create services route
@app.route("/services")
def services():
    return "This is the services page"
@app.route("/object")
def object():
    car={
        "Name":"Subaru Impreza",
        "Model":"Impreza",
        "YOM":1989
    }
    return jsonify(car)

@app.route("/home")
def home():
    # render template
    return render_template("index.html")


# run the app
if '__main__'==__name__:
    app.run(debug=True)