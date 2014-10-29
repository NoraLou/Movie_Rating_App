from flask import Flask, render_template, redirect, request, flash, session
import model


app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route("/")
def index():
    return render_template("index.html")

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
    u.password = request.form.get('password')

    if u.email == '':
        flash("Your email is required to sign up.")
        return redirect("/signup")

    # save user to the database
    model.session.add(u)
    model.session.commit()

    flash("Success! You have signed up.")
    return render_template("index.html")

@app.route("/login", methods= ['POST', 'GET'])
def login():

    #Only worked when we had post as a parameter in the form method - WHY?
    check_email = request.form.get('user_email')
    check_password = request.form.get('user_password')


    # query the database user info (email and password)

    user = model.session.query(model.User).filter_by(email = check_email).filter_by(password = check_password).first()

    if user != None:     

        # add the user id to the session
        session['user'] = user.id
        flash("Your logged in!!!!")
        return redirect("/")
        
    else:

        flash('You don\'t seem to be signed up. Please sign up below')
        return redirect('/')






if __name__ == "__main__":
    app.run(debug = True)
