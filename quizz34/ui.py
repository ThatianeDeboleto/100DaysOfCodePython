from tkinter import *
from quiz_brain import QuizBrain

COR_FUNDO = "#000000"

#OPP Dias 17 e 22
class InterfaceQuiz:

    def __init__(self, quiz_perguntas: QuizBrain):
        self.quiz = quiz_perguntas
        #propriedade de classe window + self
        self.window = Tk()
        self.window.title("Quiz para aprender!!!")
        #configurando tkinter para a vizualização do usuário
        self.window.config(padx=20, pady=20, bg=COR_FUNDO)
        #score de pontuação para as questões
        self.score_label = Label(text="Score: 0", fg="white", bg=COR_FUNDO)
        self.score_label.grid(row=0, column=1)
        #criar uma tela para as perguntas - cor diferente do fundo do tk
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=COR_FUNDO,
            font=("Arial", 20, "italic")
        )
        #pady acrescentar espaçamento tela para encaixe dos botoes
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="imagens/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="imagens/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Você chegou ao final do teste.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)








