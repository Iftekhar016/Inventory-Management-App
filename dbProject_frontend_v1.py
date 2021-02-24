# ********* PLANNED FEATURES *********

# 1.) Allow users to create and manage multiple databases.
#     Do this by showing an intro screen which will allow users to either create a new database or select existing database

# 2.) Implement "viewAll" function by default so that it is always on. Users will not have to press the button
#     This will also make sure that users don't have to click the "View All" button after updating or deleting database

# 3.) Clean up UI and fix the issue of displaying incorrect numbers next to items.
#
# ********* END *********

from tkinter import *
import dbProject_backend as bk


def getSelection(event):

    try:
        index = booksList.curselection()[0]
        global curTuple
        curTuple = booksList.get(index)

        titleEntryBox.delete(0, END)
        titleEntryBox.insert(END, curTuple[1])

        authorEntryBox.delete(0, END)
        authorEntryBox.insert(END, curTuple[2])

        yearEntryBox.delete(0, END)
        yearEntryBox.insert(END, curTuple[3])

        isbnEntryBox.delete(0, END)
        isbnEntryBox.insert(END, curTuple[4])

    except IndexError:
        pass


def viewButton():
    booksList.delete(0, END)

    for books in bk.viewAll():
        booksList.insert(END, books)


def search_Button():
    booksList.delete(0, END)

    for results in bk.search(titleEntry.get(), authorEntry.get(), yearEntry.get(), isbnEntry.get()):
        booksList.insert(END, results)


def add_button():
    bk.insert(titleEntry.get(), authorEntry.get(),
              yearEntry.get(), isbnEntry.get())
    booksList.delete(0, END)
    booksList.insert(END, (titleEntry.get(), authorEntry.get(),
                           yearEntry.get(), isbnEntry.get()))


def delete_Button():
    bk.delete(curTuple[0])


def update_button():
    bk.update(curTuple[0], titleEntry.get(),
              authorEntry.get(), yearEntry.get(), isbnEntry.get())


window = Tk()
window.wm_title("Bookstore")

titleLabel = Label(window, text="Title")
titleLabel.grid(row=0, column=0)
titleEntry = StringVar()
titleEntryBox = Entry(window, textvariable=titleEntry)
titleEntryBox.grid(row=0, column=1, padx=10, pady=10)

authorLabel = Label(window, text="Author")
authorLabel.grid(row=1, column=0)
authorEntry = StringVar()
authorEntryBox = Entry(window, textvariable=authorEntry)
authorEntryBox.grid(row=1, column=1)

yearLabel = Label(window, text="Year")
yearLabel.grid(row=0, column=2)
yearEntry = StringVar()
yearEntryBox = Entry(window, textvariable=yearEntry)
yearEntryBox.grid(row=0, column=3)

isbnLabel = Label(window, text="ISBN")
isbnLabel.grid(row=1, column=2)
isbnEntry = StringVar()
isbnEntryBox = Entry(window, textvariable=isbnEntry)
isbnEntryBox.grid(row=1, column=3)

booksList = Listbox(window, height=6, width=36)
booksList.grid(row=2, column=0, rowspan=6, columnspan=2)

listScroller = Scrollbar(window)
listScroller.grid(row=2, column=2, rowspan=6)

booksList.configure(yscrollcommand=listScroller.set)
listScroller.configure(command=booksList.yview)

booksList.bind('<<ListboxSelect>>', getSelection)

viewAllButton = Button(window, text="View All", width="12", command=viewButton)
viewAllButton.grid(row=2, column=3, padx=10, pady=5)

searchButton = Button(window, text="Search", width="12", command=search_Button)
searchButton.grid(row=3, column=3, padx=10, pady=5)

addButton = Button(window, text="Add", width=12, command=add_button)
addButton.grid(row=4, column=3, padx=10, pady=5)

updateButton = Button(window, text="Update", width="12", command=update_button)
updateButton.grid(row=5, column=3, padx=10, pady=5)

deleteButton = Button(window, text="Delete", width="12", command=delete_Button)
deleteButton.grid(row=6, column=3, padx=10, pady=5)

closeButton = Button(window, text="Close", width="12", command=window.destroy)
closeButton.grid(row=7, column=3, padx=10, pady=5)

window.mainloop()
