from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questions = [Question(question) for question in question_data]
quiz = QuizBrain(questions)

game_on = True
while game_on:
    quiz.ask_question()
    if quiz.game_over():
        game_on = False
        print("Game Over. Thank you for playing")
