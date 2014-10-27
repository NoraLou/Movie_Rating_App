import model 
import csv

def load_users(session):
    # use u.user
    f1 = csv.reader(open("./seed_data/u.user"), delimiter="|")

    for row in f1:

        # '7', 'M', 'administrator', '57', '91344'

        user = model.User()
        user.id = int(row[0])
        user.age = int(row[1])
        user.gender = row[2]
        user.occupation = row[3]
        user.zipcode = row[4]

        session.add(user)

    session.commit()

def load_movies(session):
    # use u.item

    f2 = csv.reader(open("./seed_data/u.item"), delimiter="|")  
    # movie id | movie title | release date |

    for row in f2:

        movie = model.Movie()
        movie.id = int(row[0])
        movie_title = row[1]
        movie.movie_title = movie_title.decode('latin-1')
        movie.release_date = row[2]

        session.add(movie) 

    session.commit()


def load_ratings(session):
    # use u.data
    # user id | item id | rating | timestamp. 
    f3 = csv.reader(open("./seed_data/u.data"), delimiter="\t")

    for row in f3:

        rating = model.Rating()
        rating.user_id = int(row[0])
        rating.movie_id = int(row[1])
        rating.rating = int(row[2])
        rating.timestamp = int(row[3])

        session.add(rating) 
    
    session.commit()


def main():
    # You'll call each of the load_* functions with the session as an argument
    
    load_users(session)
    load_movies(session)
    load_ratings(session)


if __name__ == "__main__":
    session = model.connect()
    main()
    

    


