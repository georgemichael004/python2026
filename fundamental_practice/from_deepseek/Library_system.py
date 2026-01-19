books = {
    "B001": {"title": "1984", "author": "Orwell", "available": True},
    "B002": {"title": "Dune", "author": "Herbert", "available": False}
}

borrowers = {
    "U001": {"name": "Alice", "borrowed_books": ["B002"]},
    "U002": {"name": "Bob", "borrowed_books": []}
}



def borrow_book(book_id, borrower_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        borrowers[borrower_id]["borrowed_books"].append(book_id)    
    else:
        print("Book not available for borrowing.")

    if len(borrowers[borrower_id]["borrowed_books"]) >= 3:
        print("Borrower already has 3 books.")

def return_book(book_id, borrower_id):
    if book_id in books and borrower_id in borrowers:
        books[book_id]["available"] = True
        borrowers[borrower_id]["borrowed_books"].remove(book_id)
    else:
        print("Invalid book ID or borrower ID.")

def find_available_books_by_author(author):
    available_books = []
    for book_id, book_info in books.items():
        if book_info["author"] == author and book_info["available"]:
            available_books.append(book_id)
    return available_books

def get_borrower_status(borrower_id):
    if borrower_id not in borrowers:        
        return "Borrower not found."
    borrowed_titles = []

    for book_id in borrowers[borrower_id]["borrowed_books"]:
        borrowed_titles.append(books[book_id]["title"])
        return {"name": borrowers[borrower_id]["name"], "borrowed_titles": borrowed_titles}