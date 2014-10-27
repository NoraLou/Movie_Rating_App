from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, autoincrement=False)
    age = Column(Integer, nullable = True)
    gender = Column(String(64), nullable = True)
    occupation = Column(String(64), nullable=True) 
    zipcode = Column(String(15), nullable=True)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key = True, autoincrement=False)
    movie_title = Column(String(64))
    release_date = Column(Integer)

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer, nullable=True)
    timestamp = Column(Integer)

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()


def main():
    """In case we need this for something"""

    engine = create_engine("sqlite:///ratings.db", echo=True)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    main()
