import sqlite3 as sq


def connect():
    connection = sq.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()


def insert(title, author, year, isbn):
    connection = sq.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def viewAll():
    connection = sq.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    results = cursor.fetchall()
    connection.close()

    return results


def search(title="", author="", year="", isbn=""):
    connection = sq.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))

    results = cursor.fetchall()
    return results


def update(id, title, author, year, isbn):
    connection = sq.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",
                   (title, author, year, isbn, id))

    connection.commit()
    connection.close()


def delete(id):
    connection = sq.connect("Books.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    connection.commit()
    connection.close()


connect()
