from typing import List

class SimpleChatbot:
    def __init__(self, questions: List[str]):
        self.questions = questions
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self) -> str:
        if self.index >= len(self.questions):
            raise StopIteration
        question = self.questions[self.index]
        self.index += 1
        return question
    
bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
iterator = iter(bot)

while True:
    try:
        question = next(iterator)
        print(question)
        input()
    except StopIteration:
        print("StopIteration Exception.")
        break