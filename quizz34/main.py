from question_model import Pergunta
from data import question_data
from quiz_brain import QuizBrain
from ui import InterfaceQuiz

banco_questoes = []
for questoes in question_data:
    question_text = questoes["question"]
    question_answer = questoes["correct_answer"]
    new_question = Pergunta(question_text, question_answer)
    banco_questoes.append(new_question)

#chamando a função
quiz = QuizBrain(banco_questoes)
quiz_ui = InterfaceQuiz(quiz)
