from tkinter import *


# def kmToMile():
#     result.insert(END, float(e1Val.get()) * 1.6)


# window = Tk()
# button = Button(window, text="Execute", command=kmToMile)
# button.grid(row=0, column=0, rowspan=2)

# e1Val = StringVar()
# e1 = Entry(window, textvariable=e1Val)
# e1.grid(row=0, column=1)

# result = Text(window, height=1, width=20)
# result.grid(row=0, column=2)
# window.mainloop()


def calcVals():

    # Deletes the content of the Text box from start to END
    # Fill in the text box with the value of gram variable
    gramText.delete("1.0", END)
    gramText.insert(END, "")
    lbText.delete("1.0", END)
    lbText.insert(END, "")
    ozText.delete("1.0", END)
    ozText.insert(END, "")

    gramText.insert(END, float(entryVal.get()) * 1000)
    lbText.insert(END, float(entryVal.get()) * 2.202462)
    ozText.insert(END, float(entryVal.get()) * 35.274)


window = Tk()

label = Label(window, text="km")
label.grid(row=0, column=0)

entryVal = StringVar()
entry = Entry(window, textvariable=entryVal)
entry.grid(row=0, column=1)

button = Button(window, text="Calculate", command=calcVals)
button.grid(row=0, column=2)

gramLabel = Label(window, text="Grams")
gramLabel.grid(row=1, column=0)


gramText = Text(window, height=1, width=20)
gramText.grid(row=1, column=1)

lbLabel = Label(window, text="Pounds")
lbLabel.grid(row=2, column=0)


lbText = Text(window, height=1, width=20)
lbText.grid(row=2, column=1)

ozLabel = Label(window, text="Ounces")
ozLabel.grid(row=3, column=0)


ozText = Text(window, height=1, width=20)
ozText.grid(row=3, column=1)

window.mainloop()
