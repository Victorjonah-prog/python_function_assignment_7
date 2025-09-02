"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = []

def add_book(**books):
    if books  in library:
        return f"{books} already exist"
    else:
        library.append(books) 
        return f"{books["title"]} added successfully"
print(add_book(id=1,title="gifted hands",author="ben carson",available=True))
print(add_book(id=2, title="The Alchemist", author="Paulo Coelho", available=True))  
print(library)        

"""Add a new book into the library with flexible details.
        return "Book {book_title} added successfully!"
"""

def search_books(search_param):
    for book in library:
        if ("title" in book and search_param in book["title"].lower()) or \
           ("author" in book and search_param in book["author"].lower()):
            return book["title"]
        else:
            return f"book doesnt exist"   
print(search_books("ben carson"))   
"""Search for books by multiple keywords (title, author).
    return books that match search description.
"""

def borrow_book(book_id):
    for book in library:
        if book["id"] == book_id:
            if "available" not in book or book["available"]:
                book["available"] = False
                return f"Book '{book['title']}' borrowed successfully"
            else:
                return f"Book '{book['title']}' is not available"
    return f"Book with ID {book_id} does not exist"
print(borrow_book(2))    

    
"""Borrow a book if available (msg: You borrowed {book_title}).
        else-> msg: Book {book_title} not available
"""
