import random
import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

randomWord = {}
afterCall = None

try:
    myData = pd.read_csv("data/to_learn.csv")
    print("Using less words file")
except FileNotFoundError:
    print("Using 200 words file")
    myData = pd.read_csv("data/polish_words.csv")
finally:
    words = myData.to_dict(orient="records")


def update_labels(lang):
    global polText, lanText

    if lang == "en":
        image = bImg
        text = "English"
    else:
        image = fImg
        text = "Polish"

    fConvas.create_image(425, 325, image=image)
    fConvas.delete(lanText)
    lanText = fConvas.create_text(425, 225, text=text, font=("Arial", 32, "italic"))

    fConvas.delete(polText)
    polText = fConvas.create_text(425, 375, text=f"{randomWord[text]}", font=("Arial", 32, "bold"))


def show_english():
    update_labels("en")


def update_word():
    global randomWord, afterCall

    if afterCall is not None:
        window.after_cancel(afterCall)

    randomWord = random.choice(words)

    update_labels("po")

    afterCall = window.after(5000, func=show_english)


def remove_word():
    global randomWord, afterCall

    words.remove(randomWord)
    randomWord = random.choice(words)

    update_labels("po")

    myDf = pd.DataFrame(words)
    myDf.to_csv("data/to_learn.csv", index=False)

    afterCall = window.after(3000, func=show_english)


window = tk.Tk()
window.minsize(width=900, height=700)
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Canvas
fConvas = tk.Canvas(width=825, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
fImg = tk.PhotoImage(file="images/card_front.png")
bImg = tk.PhotoImage(file="images/card_back.png")
fConvas.create_image(425, 325, image=fImg)
lanText = fConvas.create_text(425, 225, text="", font=("Arial", 32, "italic"))
polText = fConvas.create_text(425, 375, text="", font=("Arial", 32, "bold"))
fConvas.grid(row=1, column=1, columnspan=2)

# wrong Btn
wImg = tk.PhotoImage(file="images/wrong.png")
wBtn = tk.Button(image=wImg, highlightthickness=0, command=update_word)
wBtn.grid(row=2, column=1)

rImg = tk.PhotoImage(file="images/right.png")
rBtn = tk.Button(image=rImg, highlightthickness=0, command=remove_word)
rBtn.grid(row=2, column=2)

# For displaying card for first time
update_word()

window.mainloop()
