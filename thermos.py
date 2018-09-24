from flask import Flask, jsonify, request, Response, render_template,redirect,url_for, flash
from datetime import datetime
from logging import DEBUG
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = b'x\x8au\xd1?f\x18|\xbe\xf0H^\xc4\xf3\xd3\x12\x90)\x1e:\xd3\xcfq\xbb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///' + os.path.join(basedir,'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return "{} {}".format(self.firstname,self.lastname)

bookmarks =[]

def store_bookmarks(url):
    bookmarks.append(dict(
        url = url,
        user = 'reindert',
        date = datetime.utcnow()
    ))

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html',title='Jinja',value=User('Ritesh','Dalvi').__str__())

@app.route("/add", methods=['GET', 'POST'])
def add_bookmark():
    if request.method == "POST":
        url_to_be_bookmarked = request.form['url']; #url is the name of the text input in the form.
        store_bookmarks(url_to_be_bookmarked)
        flash('Stored Url:'+url_to_be_bookmarked)
        return redirect(url_for('index'))
    return render_template('add.html')   

@app.errorhandler(400)
def page_not_found():
    return render_template('400.html'), 400

@app.errorhandler(500)
def server_error():
    return render_template('500.html'), 500    

app.run(port = 5000, debug=True)