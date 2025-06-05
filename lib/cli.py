import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.models.models import User, Exercise, PracticeSession, Goal, Base

engine = create_engine('sqlite:///drum_practice_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    while True:
        print("\nDrum Practice Tracker CLI")
        print("1. Manage Users")
        print("2. Manage Exercises")
        print("3. Manage Practice Sessions")
        print("4. Manage Goals")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            user_menu()
        elif choice == '2':
            exercise_menu()
        elif choice == '3':
            practice_session_menu()
        elif choice == '4':
            goal_menu()
        elif choice == '5':
            print("Goodbye!")
            session.close()
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    while True:
        print("\nUser Management")
        print("1. Create User")
        print("2. Delete User")
        print("3. Display All Users")
        print("4. View User's Exercises")
        print("5. Find User by Name")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == '1':
            create_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            view_user_exercises()
        elif choice == '5':
            find_user_by_name()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def exercise_menu():
    while True:
        print("\nExercise Management")
        print("1. Create Exercise")
        print("2. Delete Exercise")
        print("3. Display All Exercises")
        print("4. View Exercise's Practice Sessions")
        print("5. Find Exercise by Name")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == '1':
            create_exercise()
        elif choice == '2':
            delete_exercise()
        elif choice == '3':
            display_all_exercises()
        elif choice == '4':
            view_exercise_sessions()
        elif choice == '5':
            find_exercise_by_name()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def practice_session_menu():
    while True:
        print("\nPractice Session Management")
        print("1. Create Practice Session")
        print("2. Delete Practice Session")
        print("3. Display All Practice Sessions")
        print("4. View Sessions by User")
        print("5. Find Session by ID")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == '1':
            create_practice_session()
        elif choice == '2':
            delete_practice_session()
        elif choice == '3':
            display_all_practice_sessions()
        elif choice == '4':
            view_sessions_by_user()
        elif choice == '5':
            find_session_by_id()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def goal_menu():
    while True:
        print("\nGoal Management")
        print("1. Create Goal")
        print("2. Delete Goal")
        print("3. Display All Goals")
        print("4. View Goals by User")
        print("5. Find Goal by Title")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        if choice == '1':
            create_goal()
        elif choice == '2':
            delete_goal()
        elif choice == '3':
            display_all_goals()
        elif choice == '4':
            view_goals_by_user()
        elif choice == '5':
            find_goal_by_title()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# Stub functions for user actions
from lib.helpers import get_non_empty_string, confirm_action

def create_user():
    name = get_non_empty_string("Enter user name: ")
    email = get_non_empty_string("Enter user email: ")
    from datetime import datetime
    created_at = datetime.now()
    user = User(name=name, email=email, created_at=created_at)
    session.add(user)
    session.commit()
    print(f"User '{name}' created successfully.")

def delete_user():
    display_all_users()
    user_id = input("Enter the ID of the user to delete: ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        if confirm_action(f"Are you sure you want to delete user '{user.name}'?"):
            session.delete(user)
            session.commit()
            print("User deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("User not found.")

def display_all_users():
    users = session.query(User).all()
    if users:
        print("\nUsers:")
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Created At: {user.created_at}")
    else:
        print("No users found.")

def view_user_exercises():
    display_all_users()
    user_id = input("Enter the ID of the user to view exercises: ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        exercises = user.exercises
        if exercises:
            print(f"\nExercises for user '{user.name}':")
            for ex in exercises:
                print(f"ID: {ex.id}, Name: {ex.name}, Type: {ex.type}, Difficulty: {ex.difficulty}")
        else:
            print("No exercises found for this user.")
    else:
        print("User not found.")

def find_user_by_name():
    name = get_non_empty_string("Enter the name to search for: ")
    users = session.query(User).filter(User.name.ilike(f"%{name}%")).all()
    if users:
        print("\nMatching Users:")
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print("No users found with that name.")

def create_exercise():
    name = get_non_empty_string("Enter exercise name: ")
    type_ = get_non_empty_string("Enter exercise type (e.g. groove, rudiment, fill): ")
    difficulty = get_non_empty_string("Enter difficulty level: ")
    user_id = input("Enter user ID for this exercise: ")
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("User not found. Exercise not created.")
        return
    exercise = Exercise(name=name, type=type_, difficulty=difficulty, user_id=user_id)
    session.add(exercise)
    session.commit()
    print(f"Exercise '{name}' created successfully.")

def delete_exercise():
    display_all_exercises()
    exercise_id = input("Enter the ID of the exercise to delete: ")
    exercise = session.query(Exercise).filter_by(id=exercise_id).first()
    if exercise:
        if confirm_action(f"Are you sure you want to delete exercise '{exercise.name}'?"):
            session.delete(exercise)
            session.commit()
            print("Exercise deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Exercise not found.")

def display_all_exercises():
    exercises = session.query(Exercise).all()
    if exercises:
        print("\nExercises:")
        for ex in exercises:
            print(f"ID: {ex.id}, Name: {ex.name}, Type: {ex.type}, Difficulty: {ex.difficulty}, User ID: {ex.user_id}")
    else:
        print("No exercises found.")

def view_exercise_sessions():
    display_all_exercises()
    exercise_id = input("Enter the ID of the exercise to view practice sessions: ")
    exercise = session.query(Exercise).filter_by(id=exercise_id).first()
    if exercise:
        sessions = exercise.practice_sessions
        if sessions:
            print(f"\nPractice Sessions for exercise '{exercise.name}':")
            for s in sessions:
                print(f"ID: {s.id}, Duration: {s.duration} mins, BPM: {s.bpm}, Date: {s.date}")
        else:
            print("No practice sessions found for this exercise.")
    else:
        print("Exercise not found.")

def find_exercise_by_name():
    name = get_non_empty_string("Enter the name to search for: ")
    exercises = session.query(Exercise).filter(Exercise.name.ilike(f"%{name}%")).all()
    if exercises:
        print("\nMatching Exercises:")
        for ex in exercises:
            print(f"ID: {ex.id}, Name: {ex.name}, Type: {ex.type}, Difficulty: {ex.difficulty}")
    else:
        print("No exercises found with that name.")

def create_practice_session():
    user_id = input("Enter user ID: ")
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("User not found. Practice session not created.")
        return
    exercise_id = input("Enter exercise ID: ")
    exercise = session.query(Exercise).filter_by(id=exercise_id).first()
    if not exercise:
        print("Exercise not found. Practice session not created.")
        return
    duration = input("Enter duration in minutes: ")
    bpm = input("Enter BPM: ")
    notes = input("Enter notes: ")
    date = input("Enter date (YYYY-MM-DD): ")
    session_obj = PracticeSession(user_id=user_id, exercise_id=exercise_id, duration=duration, bpm=bpm, notes=notes, date=date)
    session.add(session_obj)
    session.commit()
    print("Practice session created successfully.")

def delete_practice_session():
    display_all_practice_sessions()
    session_id = input("Enter the ID of the practice session to delete: ")
    psession = session.query(PracticeSession).filter_by(id=session_id).first()
    if psession:
        if confirm_action(f"Are you sure you want to delete practice session ID '{psession.id}'?"):
            session.delete(psession)
            session.commit()
            print("Practice session deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Practice session not found.")

def display_all_practice_sessions():
    sessions = session.query(PracticeSession).all()
    if sessions:
        print("\nPractice Sessions:")
        for s in sessions:
            print(f"ID: {s.id}, User ID: {s.user_id}, Exercise ID: {s.exercise_id}, Duration: {s.duration} mins, BPM: {s.bpm}, Date: {s.date}")
    else:
        print("No practice sessions found.")

def view_sessions_by_user():
    display_all_users()
    user_id = input("Enter the ID of the user to view practice sessions: ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        sessions = user.practice_sessions
        if sessions:
            print(f"\nPractice Sessions for user '{user.name}':")
            for s in sessions:
                print(f"ID: {s.id}, Exercise ID: {s.exercise_id}, Duration: {s.duration} mins, BPM: {s.bpm}, Date: {s.date}")
        else:
            print("No practice sessions found for this user.")
    else:
        print("User not found.")

def find_session_by_id():
    session_id = input("Enter the ID of the practice session to find: ")
    psession = session.query(PracticeSession).filter_by(id=session_id).first()
    if psession:
        print(f"ID: {psession.id}, User ID: {psession.user_id}, Exercise ID: {psession.exercise_id}, Duration: {psession.duration} mins, BPM: {psession.bpm}, Date: {psession.date}")
    else:
        print("Practice session not found.")

def create_goal():
    user_id = input("Enter user ID: ")
    user = session.query(User).filter_by(id=user_id).first()
    if not user:
        print("User not found. Goal not created.")
        return
    title = get_non_empty_string("Enter goal title: ")
    description = input("Enter goal description: ")
    target_bpm = input("Enter target BPM: ")
    target_duration = input("Enter target duration (minutes): ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    goal = Goal(user_id=user_id, title=title, description=description, target_bpm=target_bpm, target_duration=target_duration, deadline=deadline)
    session.add(goal)
    session.commit()
    print("Goal created successfully.")

def delete_goal():
    display_all_goals()
    goal_id = input("Enter the ID of the goal to delete: ")
    goal = session.query(Goal).filter_by(id=goal_id).first()
    if goal:
        if confirm_action(f"Are you sure you want to delete goal '{goal.title}'?"):
            session.delete(goal)
            session.commit()
            print("Goal deleted successfully.")
        else:
            print("Deletion cancelled.")
    else:
        print("Goal not found.")

def display_all_goals():
    goals = session.query(Goal).all()
    if goals:
        print("\nGoals:")
        for g in goals:
            print(f"ID: {g.id}, Title: {g.title}, User ID: {g.user_id}, Target BPM: {g.target_bpm}, Target Duration: {g.target_duration}, Deadline: {g.deadline}")
    else:
        print("No goals found.")

def view_goals_by_user():
    display_all_users()
    user_id = input("Enter the ID of the user to view goals: ")
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        goals = user.goals
        if goals:
            print(f"\nGoals for user '{user.name}':")
            for g in goals:
                print(f"ID: {g.id}, Title: {g.title}, Target BPM: {g.target_bpm}, Target Duration: {g.target_duration}, Deadline: {g.deadline}")
        else:
            print("No goals found for this user.")
    else:
        print("User not found.")

def find_goal_by_title():
    title = get_non_empty_string("Enter the title to search for: ")
    goals = session.query(Goal).filter(Goal.title.ilike(f"%{title}%")).all()
    if goals:
        print("\nMatching Goals:")
        for g in goals:
            print(f"ID: {g.id}, Title: {g.title}, User ID: {g.user_id}")
    else:
        print("No goals found with that title.")

if __name__ == '__main__':
    main_menu()
