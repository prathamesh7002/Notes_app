from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
NOTES_FILE = "notes.txt"

# Function to read notes from the text file
def read_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            notes = [line.strip().split("::") for line in file.readlines()]
        return notes
    except FileNotFoundError:
        return []

# Function to write a new note to the text file
def write_note(title, content):
    with open(NOTES_FILE, "a") as file:
        file.write(f"{title}::{content}\n")

# Function to delete a note from the text file
def delete_note(index):
    notes = read_notes()
    if 0 <= index < len(notes):
        del notes[index]
        with open(NOTES_FILE, "w") as file:
            for note in notes:
                file.write(f"{note[0]}::{note[1]}\n")

@app.route('/')
def home():
    notes = read_notes()
    return render_template('index.html', notes=notes)  # Changed from 'home.html' to 'index.html'

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        write_note(title, content)
        return redirect(url_for('home'))
    return render_template('add_note.html')

@app.route('/delete/<int:note_id>')
def delete_note_route(note_id):
    delete_note(note_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)