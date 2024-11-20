class Question:
    def __init__(self, question_id, question_stem, correct_answer):
        self.question_id = question_id
        self.question_stem = question_stem
        self.correct_answer = correct_answer.lower()

    def __str__(self):
        return f"({self.question_id}) {self.question_stem}[{self.correct_answer}]"

    def is_correct(self,attempt):
        attempt = attempt.lower()
        return self.correct_answer == attempt

class Student:
    def __init__(self, student_name, ):
        self.student_name = student_name
        self.questions = []

    def add_question(self,q):
        self.questions.append(q)

    def get_number_of_questions(self):
        return len(self.questions)

    def calculate_score(self, answers):
        score = 0

        for question, answer in zip(self.questions, answers):
            # Compare the provided answer (converted to lowercase) with the correct answer
            if answer.lower() == question.correct_answer:
                score += 1  # Increment score for each correct answer

        return score