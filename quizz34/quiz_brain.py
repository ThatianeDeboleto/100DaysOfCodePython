import html


class QuizBrain:

    def __init__(self, q_list):
        self.numero_questoes = 0
        self.score = 0
        self.lista_questoes = q_list
        self.questao_atual = None

    def still_has_questions(self):
        return self.numero_questoes < len(self.lista_questoes)

    def next_question(self):
        self.questao_atual = self.lista_questoes[self.numero_questoes]
        self.numero_questoes += 1
        # entidades do HTML - numeros, codigos, * no console em meio a resposta
        q_text = html.unescape(self.questao_atual.text)
        return f"Q.{self.numero_questoes}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.questao_atual.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False




