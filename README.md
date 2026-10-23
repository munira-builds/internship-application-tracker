# Internship Application Tracking System

A simple web application built to manage and track internship applications in one place.

## Features
- Add internship applications with company name, role, application date, status, and link.
- View all saved applications.
- Track application statistics through dashboard counters.
- Delete applications when needed.
- Store application data using SQLite.

## Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS

## Project Structure
```text
internship-application-tracker/
├── app.py
├── internships.db
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## How to Run Locally

1. Clone or download this repository.
2. Open the project folder in a terminal.
3. Install the dependencies:

   `pip install -r requirements.txt`

4. Run the application:

   `python app.py`

5. Open `http://127.0.0.1:5000` in your browser.

## What I Learned
- Building a web application with Flask.
- Connecting a Python application to an SQLite database.
- Performing database operations to add, view, and delete records.
- Organizing HTML templates and CSS files in a Flask project.

## Future Improvements
- Add application editing.
- Add search and filtering.
- Deploy the application online.
