from sqlalchemy import create_engine
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.models import Base

engine = create_engine('sqlite:///drum_practice_tracker.db')

def setup_database():
    Base.metadata.create_all(engine)
    print("Database created successfully.")

if __name__ == '__main__':
    setup_database()
