from flask import Flask, render_template, redirect, request
import model


app = Flask(__name__)

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup")
def signup():

    return render_template("signup.html")


@app.route("/newuser" method=['POST'])
def new_user():

    email = request.form("email")
    age = request.form("age")
    gender = request.form("gender")
    occupation = request.form("occupation")
    zipcode = request.form("zipcode")

    u = User(age, gender, occupation, zipcode, email)
#redirect method

    pass 


if __name__ == "__main__":
    app.run(debug = True)