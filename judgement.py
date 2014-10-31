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
        flash("You are logged in!")
        return redirect("/userpersonalratings") 

    else:

        flash('You don\'t seem to be signed up. Please sign up below')
        return redirect('/')

@app.route("/ratemovies", methods=['GET', 'POST'])
def personal_ratings():
    
    #personal_ratings = model.session.query(model.Rating).filter_by(user_id = session['user']).all()

    #user_id = session['user']

    movie_rating = request.form.get('movierating')

    movies = model.session.query(model.Movie).limit(50)

    print "*************************"
    print movie_rating
    print "*************************"

    
    return render_template("ratemovies.html", movies=movies)



@app.route("/allusers")
def show_all_users():
    users = model.session.query(model.User).all()
    return render_template('user_list.html', users = users)

@app.route('/usermovieratings')
def show_user_movie_ratings():
    #get the user id
    user_id = request.args.get("user_id")

    #query the database Ratings for movies & ratings filtered by user id

    user_ratings = model.session.query(model.Rating).filter_by(user_id = user_id).all()

    # print (dir(user_ratings[0]))

    #return objects from query to the template

    return render_template('usermovieratings.html', ratings=user_ratings, user=user_id)

    




if __name__ == "__main__":
    app.run(debug = True)
