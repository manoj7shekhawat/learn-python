import tkinter as tk

window = tk.Tk()
window.title("My title")
window.minsize(width=500, height=300)


def btnClicked():
    myLabel.config(text=myEntry.get())
    print("the text is", myEntry.get())


# LABEL
myLabel = tk.Label(text="My label", font=('Arial', 20, 'bold'))
#myLabel.pack(side="bottom")
myLabel.grid(row=1, column=1)


# Button
myButton = tk.Button(text="Click Me", command=btnClicked)
#myButton.pack()
myButton.grid(row=2, column=2)

myButton2 = tk.Button(text="New Button")
myButton2.grid(row=1, column=3)

# Entry
myEntry = tk.Entry(width=10)
#myEntry.pack()
myEntry.grid(row=3, column=4)


window.mainloop()
