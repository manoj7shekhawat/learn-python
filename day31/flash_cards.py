import tkinter as tk


BACKGROUND_COLOR = "#B1DDC6"


window = tk.Tk()
window.minsize(width=300, height=300)
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)


# Canvas
fConvas = tk.Canvas()
fImg = tk.PhotoImage(file="images/card_front.png")
fConvas.create_image(100, 100, image=fImg)
fConvas.grid(row=1, column=1, columnspan=2)


# Label Polish
pLabel = tk.Label(text="Polish", font=("Arial", 20, "italic"))
pLabel.place(x=115, y=50)

# Label Polish word
ptLabel = tk.Label(text="Jestes", font=("Arial", 32, "italic"))
ptLabel.place(x=100, y=100)

# wrong Btn
wImg = tk.PhotoImage(file="images/wrong.png")
wBtn = tk.Button(image=wImg, highlightthickness=0)
wBtn.grid(row=2, column=1)

rImg = tk.PhotoImage(file="images/right.png")
rBtn = tk.Button(image=rImg, highlightthickness=0)
rBtn.grid(row=2, column=2)

window.mainloop()