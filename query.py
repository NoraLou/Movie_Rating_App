import model

def oldmovies():

    query = session.query(model.Movie).filter(model.Movie.movie_title.like('%aladdin%')).all()
  
    for item in query:
        print item.movie_title

def main():
    oldmovies()

if __name__ == '__main__':
    session = model.connect()
    main()
