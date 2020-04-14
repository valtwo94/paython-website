from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/components')
def components():
    return render_template('components.html')


@app.route('/work')
def work():
    return render_template('work.html')


@app.route('/works')
def works():
    return render_template('works.html')
