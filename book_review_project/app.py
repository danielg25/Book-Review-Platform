from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for books and reviews
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "reviews": []},
    {"id": 2, "title": "1984", "author": "George Orwell", "reviews": []},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "reviews": []}
]

@app.route('/')
def home():
    return render_template('home.html', books=books)

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        if request.method == 'POST':
            reviewer = request.form['reviewer']
            comment = request.form['comment']
            book['reviews'].append({"reviewer": reviewer, "comment": comment})
        return render_template('book_detail.html', book=book)
    return "Book not found", 404

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        new_id = len(books) + 1
        title = request.form['title']
        author = request.form['author']
        books.append({"id": new_id, "title": title, "author": author, "reviews": []})
        return redirect(url_for('home'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
