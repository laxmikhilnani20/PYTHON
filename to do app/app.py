#from flask import Flask, request, render_template
from flask import Flask,request, render_template
app = Flask(__name__)

# Initialize an empty list to store notes
notes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission to add a new note
        title = request.form['title']
        content = request.form['content']
        notes.append({'title': title, 'content': content})
        return render_template('index.html', notes=notes)
    return render_template('index.html', notes=notes)

@app.route('/save', methods=['POST'])
def save_note():
    # Handle form submission to save a note
    title = request.form['title']
    content = request.form['content']
    index = int(request.form['index'])
    notes[index]['title'] = title
    notes[index]['content'] = content
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)