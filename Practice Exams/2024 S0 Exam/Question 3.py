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


questions = [Question(1, 'What do bees make?', 'honey'), Question(2, 'What color are Smurfs?', 'Blue')]
for p in questions:
    print(p)
    print(p.is_correct('honey'))
print(type(questions[0]))
print(questions[0].is_correct('honey'))
print(questions[0].is_correct('HONEY'))