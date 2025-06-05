# 🥁 Drum Practice Tracker CLI Application

A command-line interface (CLI) application designed to help drummers track their practice sessions, exercises, and goals. This app uses Python and SQLAlchemy ORM to manage a SQLite database, providing a structured and interactive way to log and analyze drumming practice habits.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Manage users with personal profiles.
- Create and manage custom exercises (e.g., grooves, rudiments, fills).
- Log detailed practice sessions including duration, BPM, notes, and date.
- Set and track personal practice goals with deadlines.
- View and search records with flexible CLI menus.
- Data persistence using SQLite and SQLAlchemy ORM.
- Input validation and confirmation prompts for safe data management.

---

## Technologies Used

- Python 3.x
- SQLAlchemy ORM
- SQLite Database
- Pipenv for dependency management

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies using Pipenv:

   ```bash
   pipenv install
   pipenv shell
   ```

3. Initialize the database:

   ```bash
   python lib/setup_db.py
   

---

## Usage

Start the CLI application:

```bash
python lib/cli.py
```

You will be presented with a menu to manage Users, Exercises, Practice Sessions, and Goals. Navigate through the menus to create, view, find, and delete records.

---

## Project Structure

``` bash
drum-practice-tracker/
├── lib/
│   ├── cli.py              # Main CLI application
│   ├── helpers.py          # Helper functions for input validation
│   ├── setup_db.py         # Database initialization script
│   └── models/
│       ├── __init__.py     # SQLAlchemy engine and session setup
│       └── models.py       # ORM model classes
├── drum_practice_tracker.db # SQLite database file (created after setup)
├── Pipfile                 # Dependency management
├── Pipfile.lock
└── README.md
```

---

## Database Schema

- **Users**
  - id (Primary Key)
  - name
  - email
  - created_at

- **Exercises**
  - id (Primary Key)
  - name
  - type (e.g., groove, rudiment, fill)
  - difficulty
  - user_id (Foreign Key to Users)

- **Practice Sessions**
  - id (Primary Key)
  - duration (minutes)
  - bpm
  - notes
  - date
  - exercise_id (Foreign Key to Exercises)
  - user_id (Foreign Key to Users)

- **Goals**
  - id (Primary Key)
  - title
  - description
  - target_bpm
  - target_duration (minutes)
  - deadline
  - user_id (Foreign Key to Users)

---

## Testing

Manual testing can be performed by running the CLI and exercising all menu options:

- Create, view, find, and delete users, exercises, practice sessions, and goals.
- Verify data integrity and relationships.
- Validate input handling and error messages.

For detailed testing instructions, refer to the testing guide provided in the project documentation.

---

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for improvements or bug fixes.

---

## License

This project is open-source and available under the MIT License.

---

Built with ❤️ for drummers who want to improve their practice habits.
