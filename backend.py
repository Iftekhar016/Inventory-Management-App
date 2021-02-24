import sqlite3 as sq


def connect(file):
    connection = sq.connect(file)
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    connection.commit()
    connection.close()


def insert(file, title, author, year, isbn):
    connection = sq.connect(file)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO inventory VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    connection.commit()
    connection.close()


def viewAll(file):
    connection = sq.connect(file)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    connection.close()

    return results


def search(file, title="", author="", year="", isbn=""):
    connection = sq.connect(file)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM inventory WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))

    results = cursor.fetchall()
    return results


def update(file, id, title, author, year, isbn):
    connection = sq.connect(file)
    cursor = connection.cursor()
    cursor.execute("UPDATE inventory SET title=?, author=?, year=?, isbn=? WHERE id=?",
                   (title, author, year, isbn, id))

    connection.commit()
    connection.close()


def delete(file, id):
    connection = sq.connect(file)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory WHERE id=?", (id,))
    connection.commit()
    connection.close()
