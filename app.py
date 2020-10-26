import sqlite3
from flask import Flask,redirect,url_for,render_template,request, jsonify
app=Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/',methods=['GET','POST'])
def home():
    return 'Hello World'

@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/books/<id>', methods=['GET'])
def api_id(id):
    print(id)
    for book in books:
        print(book["id"])
        if int(book["id"]) == int(id): return jsonify(book)




if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)