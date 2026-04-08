from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(5,2), nullable=False)
    in_stock = db.Column(db.Boolean, default=True)
    published_date = db.Column(db.String)

    
    def to_dict(self):
        return{
            'id':self.id,
            'title':self.title,
            'author':self.author,
            'price':self.price,
            'in_stock':self.in_stock,
            'published_date':self.published_date
        }
        
 