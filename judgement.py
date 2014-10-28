from flask import Flask, render_template, redirect, request, flash, session
import model


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/newuser", methods=['POST'])
def new_user():

    u = model.User()

    #python needs variables 'name' attr and not id
    u.email = request.form.get('email')
    u.age = request.form.get('age')
    u.gender = request.form.get('gender')
    u.occupation = request.form.get('occupation')
    u.zipcode = request.form.get('zipcode')

    if u.email == '':
        flash("Your email is required to sign up.")
        return redirect("/signup")

    # save user to the database
    model.session.add(u)
    model.session.commit()

    return render_template("success.html")


#redirect method



if __name__ == "__main__":
    app.run(debug = True)