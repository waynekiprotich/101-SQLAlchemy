from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Book
from datetime import datetime, date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def to_dict(self):
    return {
        'id': self.id,
        'title': self.title,
        'author': self.author,
        'price': float(self.price),
        'in_stock': self.in_stock,
        'published_date': self.published_date
    }

#HOME 
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the books'})

# READ ALL
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])

# CREATE
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()


    new_book = Book(
        id=data.get('id'),
        title=data['title'],
        author=data['author'],
        price=data['price'],
        in_stock=data.get('in_stock', True),
        published_date=data['published_date']
    )
    
    db.session.add(new_book)
    db.session.commit()
    
    return jsonify({"message": "Book added successfully!", "book": new_book.to_dict()}), 201

# READ ONE
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'error':'Book not found'}), 404
    return jsonify(book.to_dict())

# UPDATE ONE
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    
    book = Book.query.get(book_id)
    if not book:
        return {"error": "Book not found"}, 404

    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.price = data.get('price', book.price)
    book.in_stock = data.get('in_stock', book.in_stock)
    book.published_date = data.get('published_date', book.published_date)
    
    db.session.commit()
    
    return {"message": "Book updated successfully!", "book_id": book.id}, 200

# DELETE ONE
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return {"error": "Book not found"}, 404

    db.session.delete(book)
    db.session.commit()
    return {"message": f"Book with ID {book_id} deleted successfully!"}, 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(host="0.0.0.0", port=5000, debug=True)