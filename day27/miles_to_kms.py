import tkinter as tk

window = tk.Tk()
window.title("Mile to KM converter")
window.minsize(width=200, height=100)


def calculate():
    miles = int(myEntry.get())
    kms = round(1.6 * miles, 2)
    myLabel3.config(text=kms)


# Entry
myEntry = tk.Entry()
myEntry.insert(tk.END, '0')
myEntry.grid(row=1, column=2)
myEntry.config(width=10)

# Label
myLabel = tk.Label(text="Miles")
myLabel.grid(row=1, column=3)

myLabel2 = tk.Label(text="is equal to")
myLabel2.grid(row=2, column=1)

myLabel3 = tk.Label(text="0")
myLabel3.grid(row=2, column=2)

myLabel4 = tk.Label(text="Km")
myLabel4.grid(row=2, column=3)

# Button
myBtn = tk.Button(text="Calculate", command=calculate)
myBtn.grid(row=3, column=2)


window.mainloop()