import tkinter
import quiz_brain

THEME_COLOR = "#375362"
WHITE = "white"
QUESTION_FONT = ("arial", 14, "italic")


class QuizUI:
    def __init__(self, quizbrain: quiz_brain.QuizBrain):

        self.quiz = quizbrain

        self.window = tkinter.Tk()
        self.window.title = "Quizzler"
        self.window.config(
            bg=THEME_COLOR,     # window background color
            padx=20,            # window border x
            pady=20             # windows border y
        )

        self.score = tkinter.Label(
            text="Score: 0",    # label text
            bg=THEME_COLOR,     # label background color
            fg=WHITE            # label text color
        )
        self.score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg=WHITE)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question = self.canvas.create_text(
            150,                # text center x
            125,                # text center y
            width=295,
            text="question",
            font=QUESTION_FONT
        )

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="WHITE")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(
                self.question,
                text=self.quiz.next_question()
            )
            self.true_button.config(state="active")
            self.false_button.config(state="active")
        else:
            self.canvas.itemconfig(
                self.question,
                text="you reached the end of the quiz"
            )

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="GREEN")
        else:
            self.canvas.config(bg="RED")

        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(1000, self.get_next_question)
