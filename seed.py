import model 
import csv

def load_users(session):
    # use u.user
    f1 = csv.reader(open("./seed_data/u.user"), delimiter="|")

    for row in f1:

        # '7', 'M', 'administrator', '57', '91344'

        user = model.Users()
        user.user_id = int(row[0])
        user.age = int(row[1])
        user.gender = row[2]
        user.occupation = row[3]
        user.zipcode = row[4]

        session.add(user)

    session.commit()

def load_movies(session):
    # use u.item
    #       movie id | movie title | release date | video release date |


        # 1 indicates the movie
        #       is of that genre, a 0 indicates it is not; movies can be in
        #       several genres at once.
        #       The movie ids are the ones used in the u.data data set.

    pass

def load_ratings(session):
    # use u.data
    # u.data columns user id | item id | rating | timestam
    pass

def main():
    # You'll call each of the load_* functions with the session as an argument
    
    load_users(session)


if __name__ == "__main__":
    session = model.connect()
    main()
    

    


