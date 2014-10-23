from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable=True)
    zipcode = Column(String(15), nullable=True)

class Movies(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key = True)
    movie_title = Column(String(64))
    release_date = Column(Integer)

class Ratings(Base):
    __tablename__ = 'ratings'

    user_id = Column(Integer, primary_key = True)
    item_id = Column(Integer, ForeignKey('movies.movie_id'))
    rating = Column(Integer, nullable=True)
    timestamp = Column(Integer)

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()


### End class declarations

def main():
    """In case we need this for something"""
    pass


if __name__ == "__main__":
    main()
