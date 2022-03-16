import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.qb = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.scoreLabel = tk.Label(text=f"Score 0", font=('Arial', 20, 'normal'), bg=THEME_COLOR)
        self.scoreLabel.config(fg="white")
        self.scoreLabel.grid(row=0, column=1)

        # Image
        self.tImage = tk.PhotoImage(file="images/true.png")
        self.fImage = tk.PhotoImage(file="images/false.png")

        # Canvas
        self.mCanvas = tk.Canvas(height=250, width=300, bg="white")
        self.qText = self.mCanvas.create_text(
            150,
            125,
            width=230,
            text="Sample Question",
            font=('Arial', 24, 'italic'))
        self.mCanvas.grid(row=1, column=0, columnspan=2)

        # True button and False button
        self.bCanvas = tk.Canvas(height=125, width=300, bg=THEME_COLOR, highlightthickness=0)
        self.bCanvas.grid(row=2, column=0, columnspan=2)
        self.tBtn = tk.Button(image=self.tImage, highlightthickness=0, command=self.check_true_answer)
        self.tBtn.grid(row=2, column=0)
        self.fBtn = tk.Button(image=self.fImage, highlightthickness=0, command=self.check_false_answer)
        self.fBtn.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.mCanvas.config(bg="white")
        if self.qb.still_has_questions():
            ques = self.qb.next_question()
            self.mCanvas.itemconfig(self.qText, text=f"{ques}", font=('Arial', 20, 'italic'))
        else:
            self.mCanvas.itemconfig(self.qText, text=f"You have reahed to the end of Quiz",
                                    font=('Arial', 20, 'italic'))
            # Disabling buttons
            self.tBtn.config(state="disabled")
            self.fBtn.config(state="disabled")

    def check_true_answer(self):
        answer = self.qb.check_answer("True")
        self.scoreLabel.config(text=f"Score {self.qb.score}")
        if answer:
            self.mCanvas.config(bg="green")
        else:
            self.mCanvas.config(bg="red")
        self.window.after(2000, func=self.next_question)

    def check_false_answer(self):
        answer = self.qb.check_answer("False")
        self.scoreLabel.config(text=f"Score {self.qb.score}")
        if answer:
            self.mCanvas.config(bg="green")
        else:
            self.mCanvas.config(bg="red")
        self.window.after(2000, func=self.next_question)
