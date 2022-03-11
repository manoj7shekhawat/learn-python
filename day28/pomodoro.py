import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

step = 0
myAfter = None

# ---------------------------- TIMER RESET ------------------------------- #

def resetClock():
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timerText, text=f"00:00")
    window.after_cancel(myAfter)
    tick.config(text=f"")

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def startCounter():
    global step
    step += 1

    if step == 9:
        resetClock()

    if step in (1, 3, 5, 7):
        minsToRun = WORK_MIN
        label.config(text="Work", fg=GREEN)
    elif step in (2, 4, 6):
        minsToRun = SHORT_BREAK_MIN
        label.config(text="Break", fg=PINK)
    else:
        minsToRun = LONG_BREAK_MIN
        label.config(text="Break", fg=RED)

    countDown(minsToRun * 60)



def countDown(count):
    global myAfter
    mins = math.floor(count/60)
    secs = count % 60
    canvas.itemconfig(timerText, text=f"{mins:02}:{secs:02}")

    if count > 0:
        myAfter = window.after(1000, countDown, count - 1)
    else:
        startCounter()
        if step % 2 == 0:
            tick.config(text=f"{'✔'* int(step/2)}")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=325, height=325)
window.config(bg=YELLOW, padx=50, pady=25)



# Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timerText = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(row=2, column=2)

# Label
label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
label.grid(row=1, column=2)


# Start btn
sBtn = tk.Button(text="Start Me", command=startCounter)
sBtn.grid(row=3, column=1)

# Reset btn
rBtn = tk.Button(text="Reset", command=resetClock)
rBtn.grid(row=3, column=3)

# Tick
tick = tk.Label(fg="blue", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
tick.grid(row=4, column=2)


window.mainloop()