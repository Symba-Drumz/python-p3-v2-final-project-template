from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .models import User, Exercise, PracticeSession, Goal



engine = create_engine('sqlite:///drum_practice_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



__all__ = ["User", "Exercise", "PracticeSession", "Goal"]
