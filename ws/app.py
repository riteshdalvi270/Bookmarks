# this was just used for practise.

from flask import Flask, jsonify, request, Response
from validator import Validator

app = Flask(__name__)
print(__name__)

books = [
    {
        'name': 'Harry Potter',
        'price': 3.4,
        'isbn': 34234244
    },
    {
        'name': 'Real Player One',
        'price': 32.3,
        'isbn': 121212
    },
    {
        'name': 'Cat in bag',
        'price': 32.3,
        'isbn': 121212
    }
]


@app.route('/books')
def get_books():
    return jsonify({'books': books})


@app.route('/books', methods=['POST'])
def add_books():
    request_object = request.get_json()
    validator = Validator()
    if(validator.validate_json(request_object)):
        return Response("","201","")
    else:
        return False


@app.route("/books/<int:isbn>")
def get_books_by_isbn(isbn):
    results = []
    result = {}

    for book in books:
        if book['isbn'] == isbn:
            result = {'name': book['name'], 'price': book['price']}
        results.append(result)
    return jsonify(results)



#app.run(port=5000)