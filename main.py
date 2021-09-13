import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collections.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Book {self.title}'

db.create_all()

# Create a record #
new_book = Book(id=3, title="Peko Kitchen", author="Peko", rating=8)
db.session.add(new_book)
db.session.commit()

# Read a particular record by Query #
book = Book.query.filter_by(title="Harry Porter").first()

# Update a record by Primary_Key #
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Porter and the Globet of Fire"
db.session.commit()

# Delete a particular record by Primyar Key #
book_id = 1
book_to_delete = Book.query.delete(book_id)
db.session.delete(book_to_delete)
db.session.committ()


all_books = db.session.query(Book).all()
print(all_books)





# db = sqlite3.connect("new-books-collections.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         rep = f"Person({self.name}, {self.age})"
#         return rep
#
# person = Person('John', 20)
# print(person)