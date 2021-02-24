import tkinter

THEME_COLOR = "#375362"
WHITE = "white"
QUESTION_FONT = ("arial", 20, "italic")


class QuizUI:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title = "Quizzler"
        self.window.config(
            bg=THEME_COLOR,  # window background color
            padx=20,  # window border x
            pady=20  # windows border y
        )

        self.score = tkinter.Label(
            text="Score",  # label text
            bg=THEME_COLOR,  # label background color
            fg=WHITE  # label text color
        )
        self.score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question = self.canvas.create_text(
            150,  # text center x
            125,  # text center y
            text="question",
            font=QUESTION_FONT
        )

        self.true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=self.true_image)
        self.true_button.grid(row=2, column=0)

        self.false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=self.false_image)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()
