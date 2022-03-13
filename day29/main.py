import tkinter as tk
import tkinter.messagebox as mb
import random
import pyperclip as pc

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def fillPasswd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(2, 3)

    passwd = []

    passwd = [random.choice(letters) for x in range(nr_letters)]
    passwd += [random.choice(symbols) for x in range(nr_symbols)]
    passwd += [random.choice(numbers) for x in range(nr_numbers)]

    # Shuffle
    random.shuffle(passwd)

    passWord = ''.join(passwd)
    print(f"{passWord}")

    passEntry.insert(0, passWord)
    pc.copy(passWord)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addFunction():

    webSite = webEntry.get()
    passWd = passEntry.get()
    emailID = EmlEntry.get()

    line = " | ".join([webSite, emailID, passWd])

    if len(webSite) == 0 or len(passWd) == 0:
        mb.showerror(message="Please all fields")
    else:
        isOk = mb.askokcancel(title="Oops", message=f"Email: {emailID}\nPassword: {passWd}\nIs it ok?")

        if isOk:
            # Append to data.txt file
            with open("data.txt", mode="a") as fh:
                fh.write(line + "\n")
                # Clear the entry
                webEntry.delete(0, tk.END)
                passEntry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# Canvas
canvas = tk.Canvas(height=200, width=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(125, 125, image=image)
canvas.grid(row=1, column=2)

# Label
webLabel = tk.Label(text="Website:", font=("Aerial", 12, "bold"))
webLabel.grid(row=2, column=1)

# Entry
webEntry = tk.Entry(width=35)
webEntry.focus()
webEntry.grid(row=2, column=2, columnspan=2)


# EmlLabel
EmlLabel = tk.Label(text="Email/Username:", font=("Aerial", 12, "bold"))
EmlLabel.grid(row=3, column=1)

# Entry
EmlEntry = tk.Entry(width=35)
EmlEntry.insert(0, "manoj7shekhawat@gmail.com")
EmlEntry.grid(row=3, column=2, columnspan=2)

# passLabel
passLabel = tk.Label(text="Password:", font=("Aerial", 12, "bold"))
passLabel.grid(row=4, column=1)

# Entry
passEntry = tk.Entry(width=21)
passEntry.grid(row=4, column=2)

# Password btn
passBtn = tk.Button(text="Generate Password", command=fillPasswd)
passBtn.grid(row=4, column=3)

# Add btn
addBtn = tk.Button(text="Add", width=36, command=addFunction)
addBtn.grid(row=5, column=2, columnspan=2)





window.mainloop()