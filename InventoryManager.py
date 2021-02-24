import os
from tkinter import *
import backend as bk


def getSelection(event):

    try:
        index = itemsList.curselection()[0]
        global curTuple
        curTuple = itemsList.get(index)

        nameEntryBox.delete(0, END)
        nameEntryBox.insert(END, curTuple[1])

        quantityEntryBox.delete(0, END)
        quantityEntryBox.insert(END, curTuple[2])

        purchaseDateEntryBox.delete(0, END)
        purchaseDateEntryBox.insert(END, curTuple[3])

        sellPriceEntryBox.delete(0, END)
        sellPriceEntryBox.insert(END, curTuple[4])

    except IndexError:
        pass


def allEntries():
    itemsList.delete(0, END)

    for books in bk.viewAll(file):
        itemsList.insert(END, books)


def search_Button():
    itemsList.delete(0, END)

    for results in bk.search(file, nameEntry.get(), quantityEntry.get(), purchaseDateEntry.get(), sellPriceEntry.get()):
        itemsList.insert(END, results)


def add_button():
    bk.insert(file, nameEntry.get(), quantityEntry.get(),
              purchaseDateEntry.get(), sellPriceEntry.get())
    allEntries()


def delete_Button():
    bk.delete(file, curTuple[0])
    allEntries()


def update_button():
    bk.update(file, curTuple[0], nameEntry.get(),
              quantityEntry.get(), purchaseDateEntry.get(), sellPriceEntry.get())
    allEntries()


def clear_Button():
    nameEntryBox.delete(0, END)
    quantityEntryBox.delete(0, END)
    purchaseDateEntryBox.delete(0, END)
    sellPriceEntryBox.delete(0, END)


def dbWindow(file):
    global nameEntry, quantityEntry, purchaseDateEntry, sellPriceEntry
    global itemsList, purchaseDateEntryBox, nameEntryBox, sellPriceEntryBox, quantityEntryBox
    bk.connect(file)
    window = Tk()
    window.wm_title(file)

    nameLabel = Label(window, text="Name")
    nameLabel.grid(row=0, column=0)
    nameEntry = StringVar()
    nameEntryBox = Entry(window, textvariable=nameEntry)
    nameEntryBox.grid(row=0, column=1, padx=10, pady=10)

    quantityLabel = Label(window, text="Quantity")
    quantityLabel.grid(row=1, column=0)
    quantityEntry = StringVar()
    quantityEntryBox = Entry(window, textvariable=quantityEntry)
    quantityEntryBox.grid(row=1, column=1)

    purchaseDateLabel = Label(window, text="Purchase Date")
    purchaseDateLabel.grid(row=0, column=2)
    purchaseDateEntry = StringVar()
    purchaseDateEntryBox = Entry(window, textvariable=purchaseDateEntry)
    purchaseDateEntryBox.grid(row=0, column=3)

    sellPriceLabel = Label(window, text="Sell Price")
    sellPriceLabel.grid(row=1, column=2)
    sellPriceEntry = StringVar()
    sellPriceEntryBox = Entry(window, textvariable=sellPriceEntry)
    sellPriceEntryBox.grid(row=1, column=3)

    itemsList = Listbox(window, height=6, width=36)
    itemsList.grid(row=2, column=0, rowspan=6, columnspan=2)

    listScroller = Scrollbar(window)
    listScroller.grid(row=2, column=2, rowspan=6)

    itemsList.configure(yscrollcommand=listScroller.set)
    listScroller.configure(command=itemsList.yview)

    itemsList.bind('<<ListboxSelect>>', getSelection)
    allEntries()

    searchButton = Button(window, text="Search",
                          width="12", command=search_Button)
    searchButton.grid(row=2, column=3, padx=10, pady=5)

    addButton = Button(window, text="Add", width=12, command=add_button)
    addButton.grid(row=3, column=3, padx=10, pady=5)

    updateButton = Button(window, text="Update",
                          width="12", command=update_button)
    updateButton.grid(row=4, column=3, padx=10, pady=5)

    deleteButton = Button(window, text="Delete",
                          width="12", command=delete_Button)
    deleteButton.grid(row=5, column=3, padx=10, pady=5)

    clearButton = Button(window, text="Clear",
                         width="12", command=clear_Button)
    clearButton.grid(row=6, column=3, padx=10, pady=5)

    closeButton = Button(window, text="Close", width="12",
                         command=window.destroy)
    closeButton.grid(row=7, column=3, padx=10, pady=5)

    window.mainloop()


def openDB():
    global file
    file = filename.get()
    window.destroy()
    dbWindow(file)


def createNow():
    global file
    file = fileEntryName.get()
    newWindow.destroy()
    dbWindow(file)


def createDB():
    window.destroy()

    global newWindow
    global fileEntryName
    newWindow = Tk()
    label = Label(newWindow, text="Please enter new file name: ")
    label.grid(row=0, column=0, padx=10, pady=10)

    fileEntryName = StringVar()
    fileEntry = Entry(newWindow, textvariable=fileEntryName)
    fileEntry.grid(row=1, column=0)

    createNew = Button(newWindow, text="Done", width="12", command=createNow)
    createNew.grid(row=2, column=0, padx=10, pady=10)
    newWindow.mainloop()


def getter(event):
    try:
        index = dbList.curselection()[0]
        filenameEntry.delete(0, END)
        filenameEntry.insert(END, dbList.get(index))
    except:
        pass


def main():
    global dbList
    global window
    global filename
    global filenameEntry
    window = Tk()

    text = Label(window, text="Please select an option from the list: ")
    filename = StringVar()
    filenameEntry = Entry(window, textvariable=filename)
    #filenameEntry.grid(row=0, column=1)
    text.grid(row=1, column=0)

    dbList = Listbox(window, height=6, width=35)
    dbList.grid(row=1, column=1, columnspan=2)

    scroller = Scrollbar(window)
    scroller.grid(row=1, column=3)

    dbList.configure(yscrollcommand=scroller.set)
    scroller.configure(command=dbList.yview)

    dbList.bind("<<ListboxSelect>>", getter)
    for files in os.listdir():
        if files.endswith('.db'):
            dbList.insert(END, files)

    openButton = Button(window, text="Open", width=10, command=openDB)
    openButton.grid(row=2, column=1)

    createButton = Button(window, width=10, text="Create", command=createDB)
    createButton.grid(row=2, column=2)
    window.mainloop()


main()
