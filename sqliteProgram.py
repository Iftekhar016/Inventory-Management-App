import sqlite3 as sq


def createTable():
    conn = sq.connect("dummy.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sq.connect("dummy.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sq.connect("dummy.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sq.connect("dummy.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(item, quantity, price):
    conn = sq.connect("dummy.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quantity, price, item))
    conn.commit()
    conn.close()


# createTable()
# insert("Coffee", 10, 12)
# insert("Water", 5, 2)
# delete("Coffee")
# results = view()
# print(results[0][0])
# 6print(view())

update('Coffee', 11, 13)
print(view())
