import model
import csv

def load_users(session):
    # use u.user
     # user id | age O | gender 0| occupation 0 | zip code 0| username | password 
     # The user ids are the ones used in the u.data data set.
    pass

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

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    pass
    

if __name__ == "__main__":
    s= model.connect()
    main(s)
