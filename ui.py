from tkinter import *
THEME_COLOR = "#375362"
fnt=("Arial",20,"italic")
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.window=Tk()
        self.quiz=quizbrain
        self.window.title("TruthQuest")
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)
        self.canvas=Canvas(width=300, height=250)
        self.ques_text=self.canvas.create_text(150,125,text="Some text",width=280, fill=THEME_COLOR,font=fnt)
        self.canvas.grid(column=0,row=1, columnspan=2, pady=50)
        self.score_label=Label(text="Score: 0",bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1,row=0)

        img_tr=PhotoImage(file="images/true.png")
        img_fl=PhotoImage(file="images/false.png")
        self.true_bt=Button(image=img_tr,highlightthickness=0,bd=0,command=self.checkiftrue)
        self.true_bt.grid(column=1, row=2)
        self.false_bt = Button(image=img_fl,highlightthickness=0,bd=0,command=self.checkiffalse)
        self.false_bt.grid(column=0, row=2)
        self.get_nxt_quest()

        self.window.mainloop()

    def get_nxt_quest(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text, text=q_text)
        else:
            self.canvas.itemconfig(self.ques_text,text="You have reached the end of the quiz ")
            self.true_bt.config(state="disabled")
            self.false_bt.config(state="disabled")

    def checkiftrue(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def checkiffalse(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nxt_quest)

