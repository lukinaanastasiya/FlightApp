@app.route('/')
@app.route('/books')
def showBooks():
    books = session.query(Book).all()
    return render_template("output.html", books=books)


# Эта функция позволит создать новую книгу и сохранить ее в базе данных.
@app.route('/books/new/', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        newBook = Book(title=request.form['name'], author=request.form['author'], genre=request.form['genre'])
        session.add(newBook)
        session.commit()
        return redirect(url_for('showBooks'))
    else:
        return render_template('newBook.html')


# Эта функция позволит нам обновить книги и сохранить их в базе данных.
@app.route("/books/<int:book_id>/edit/", methods=['GET', 'POST'])
def editBook(book_id):
    editedBook = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedBook.title = request.form['name']
            return redirect(url_for('showBooks'))
    else:
        return render_template('editBook.html', book=editedBook)


# Эта функция для удаления книг
@app.route('/books/<int:book_id>/delete/', methods=['GET', 'POST'])
def deleteBook(book_id):
    bookToDelete = session.query(Book).filter_by(id=book_id).one()
    if request.method == 'POST':
        session.delete(bookToDelete)
        session.commit()
        return redirect(url_for('showBooks', book_id=book_id))
    else:
        return render_template('deleteBook.html', book=bookToDelete)