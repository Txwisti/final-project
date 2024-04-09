from flask import Flask, render_template, request

app = Flask(__name__)

#главная

@app.route('/')
def index():
    return render_template('index.html')

#информация

@app.route('/info')
def info():
    return render_template('info.html')

#причины

@app.route('/reasons')
def reasons():
    return render_template('reasons.html')

#научные факты

@app.route('/scientifacts')
def since():
    return render_template('scientific facts.html')

#комьюнити 

@app.route('/comunity')
def comunity():
    return render_template('comunity.html')

app.run(debug=True)