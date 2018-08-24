from flask import Flask, jsonify, request, Response, render_template,redirect,url_for

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return "{} {}".format(self.firstname,self.lastname)

bookmarks =[]

def store_bookmarks(url):
    bookmarks.append(dict{
        url: url,
        user: 'reindert'
        date: datetime.utcnow()
    })
    
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html',title='Jinja',value=User('Ritesh','Dalvi').__str__())

@app.route("/add", method =['POST', 'GET'])
def add_bookmark():
    if(request.method == "POST"):
        url_to_be_bookmarked = request.form('url'); #url is the name of the text input in the form.
        store_bookmarks(url_to_be_bookmarked)
    return render_template('add.html')   

@app.errorhandler(400)
def page_not_found():
    return render_template('400.html'), 400

@app.errorhandler(500)
def server_error():
    return render_template('500.html'), 500    

app.run(port = 5000, debug=True)