class Question:
    def __init__(self, data):
        self.question = data["text"]
        self.answer = data["answer"]

    def is_correct(self, answer):
        return answer == self.answer
