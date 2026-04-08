from app import app, db
from models import Book
from datetime import date  

with app.app_context():
    db.create_all()
    
    new_book = Book(
        title='Of Mice and Men & Cannery Row',
        author='John Steinbeck',
        price=12.99,
        in_stock=True,
        published_date='April 7, 2006'  
    )

    db.session.add(new_book)
    db.session.commit()

    print("Book added successfully!")