import sqlite3
from tkinter import *

window = Tk()

input_name = StringVar()
input_author = StringVar()
input_year = StringVar()
input_isbn = StringVar()


def quit():
    window.destroy()


with sqlite3.connect("books.db") as con:
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS books 
    (book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
     author TEXT NOT NULL,
      year INTEGER NOT NULL,
       ISBN INTEGER NOT NULL)
    ''')


    def add_book(name, author, year, isbn):
        cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (name, author, year, isbn))


    def view_books():
        cur.execute("SELECT * FROM books")
        row = cur.fetchall()
        return row


    def find_one_book(id):
        cur.execute("SELECT * FROM books WHERE book_id=?", (id))
        row = cur.fetchall()
        return row


    def update_book_by_id(id, new_name, new_author, new_year, new_isbn):
        cur.execute("UPDATE book SET name=?, author=?, year=?,ISBN=? WHERE book_id=?",
                    (new_name, new_author, new_year, new_isbn, id))


    def delete_book(id):
        cur.execute("DELETE FROM book WHERE book_id=?", (id))


    t1 = Label(window, text="Name")
    t1.grid(row=0, column=0)

    e1 = Entry(window, textvariable=input_name)
    e1.grid(row=0, column=1)

    t2 = Label(window, text="Author")
    t2.grid(row=0, column=2)

    e2 = Entry(window, textvariable=input_author)
    e2.grid(row=0, column=3)

    t3 = Label(window, text="Year")
    t3.grid(row=1, column=0)

    e3 = Entry(window, textvariable=input_year)
    e3.grid(row=1, column=1)

    t4 = Label(window, text="ISBN")
    t4.grid(row=1, column=2)

    e4 = Entry(window, textvariable=input_isbn)
    e4.grid(row=1, column=3)

    b1 = Button(window, width=10, text="ADD")
    b1.grid(row=2, column=3)

    b2 = Button(window, width=10, text="View all")
    b2.grid(row=3, column=3)

    b3 = Button(window, width=10, text="Find")
    b3.grid(row=4, column=3)

    b4 = Button(window, width=10, text="Update")
    b4.grid(row=5, column=3)

    b5 = Button(window, width=10, text="Delete")
    b5.grid(row=6, column=3)

    b6 = Button(window, width=10, text="Close",command=quit)
    b6.grid(row=7, column=3)

    l1 = Listbox(window, width=50)
    l1.grid(row=2, column=0, columnspan=3, rowspan=6)

    con.commit()
    window.mainloop()
