from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref,scoped_session


ENGINE = None
Session = None

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,autocommit = False, autoflush=False))
Base = declarative_base()
Base.query = session.query_property()



### Class declarations go here

class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable = True)
    gender = Column(String(64), nullable = True)
    occupation = Column(String(64), nullable=True) 
    zipcode = Column(String(15), nullable=True)
    email = Column(String(64), nullable=True)

# created an attribute called ratings that backref to Rating table

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key = True)
    movie_title = Column(String(64))
    release_date = Column(Integer)

# created an attribute called ratings that backref to Rating table

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer, nullable=True)
    timestamp = Column(Integer)

    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///ratings.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()

# def main():
#     """In case we need this for something"""

#     engine = create_engine("sqlite:///ratings.db", echo=True)
#     Base.metadata.create_all(engine)


# if __name__ == "__main__":
#     main()