class QuizBrain:
    def __init__(self, questions):
        self.number_correct = 0
        self.question_number = 0
        self.questions = questions
        self.current_question = self.questions[self.question_number]
    
    def display_score(self):
        print(f"You're current score is {self.number_correct} / {self.question_number}")

    def game_over(self):
        return self.question_number >= len(self.questions)

    def next_question(self):
        self.question_number += 1
        if not self.game_over():
            self.current_question = self.questions[self.question_number]
    
    def ask_question(self):
        ans = input(f"Q {self.question_number + 1}: {self.current_question.question}: True or False: ")
        if ans == self.current_question.answer:
            self.number_correct += 1
            print("Correct")
        else:
            print("Incorrect")
        self.next_question()
        self.display_score()


        

    