from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime)

    exercises = relationship("Exercise", back_populates="user")
    practice_sessions = relationship("PracticeSession", back_populates="user")
    goals = relationship("Goal", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)  # e.g. groove, rudiment, fill
    difficulty = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="exercises")
    practice_sessions = relationship("PracticeSession", back_populates="exercise")

    def __repr__(self):
        return f"<Exercise(id={self.id}, name={self.name}, type={self.type})>"

class PracticeSession(Base):
    __tablename__ = 'practice_sessions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    duration = Column(Integer)  # in minutes
    bpm = Column(Integer)
    notes = Column(Text)
    date = Column(String)  # or use Date/DateTime if preferred
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    exercise = relationship("Exercise", back_populates="practice_sessions")
    user = relationship("User", back_populates="practice_sessions")

    def __repr__(self):
        return f"<PracticeSession(id={self.id}, duration={self.duration}, bpm={self.bpm})>"

class Goal(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(Text)
    target_bpm = Column(Integer)
    target_duration = Column(Integer)  # minutes
    deadline = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="goals")

    def __repr__(self):
        return f"<Goal(id={self.id}, title={self.title}, deadline={self.deadline})>"
