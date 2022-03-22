from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')

def _get_table(db):
    return db.create_table("books",primary_id = "id",primary_type=db.types.integer)


def get_each_book_response(id,success_response_code=200 ,failure_response_code=404):
    book_obj = _get_table(db).findone(id=id)
    if book_obj:
        return make_response(jsonify(book_obj),success_response_code=200)
    else:
        return make_response(jsonify(book_obj),failure_response_code=404)



def fetch_db_all():
    books = []
    for book in _get_table:
        books.append(book)
    return books


@app.route('/api/db_populate', methods=['POST'])
def db_populate():
    table =db ["books"]
    data = {
        "id": 1,
        "name": "Abc book.",
        "author": "Kiran1"
    }
    table.insert_ignore(data,["id"])

    data = {
        "id": 2,
        "name": "Pqr book",
        "author": "Kiran2"
    }
    table.insert_ignore(data,["id"])
    return make_response("",201)


@app.route('/api/books', methods=['GET', 'POST'])
def api_books():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), success_response_code = 200)
    elif request.method == 'POST':
        content = request.json
        id = content['id']
        _get_table(db).insert(content)
        return get_each_book_response(id, success_response_code=201)  # 201 = Created
#

@app.route('/api/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_book(book_id):
    if request.method == "GET":
        return get_each_book_response(id)

    elif request.method == "PUT":
        content = request.json
        _get_table(db).update(content,["id"])
        return make_response("",204)

    elif request.method == "DELETE":
        _get_table(db).delete(id=id)
        return make_response("",204)



if __name__ == '__main__':
    app.run(debug=True)