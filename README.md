# Notes_app
# Notes App

A simple Notes application built with Flask. This app allows you to add, view, and delete notes. Notes are stored in a plain text file.

## Features

- Add new notes with a title and content
- View all saved notes
- Delete notes

## Requirements

- Python 3.x
- Flask

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/prathamesh7002/Notes_app.git
   cd Notes_app
   ```

2. **Install dependencies:**
   ```sh
   pip install flask
   ```

## Usage

1. **Run the Flask app:**
   ```sh
   python app.py
   ```

2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
notes-app/
│
├── app.py
├── notes.txt
└── templates/
    ├── base.html
    ├── home.html
    └── add_note.html
```

## How it works

- Notes are stored in `notes.txt` with each note on a new line, separated by `::`.
- The app uses Flask routes to handle adding, viewing, and deleting notes.

## License

This project is licensed under the MIT License.