from PYTHONBEGINNERS import Point 
from PYTHONBEGINNERS import Question 






Homecoordinate = Point(2,3)
print(Homecoordinate.x)
print(Homecoordinate.y)
Homecoordinate.location()

class RoomCount(Point):
    def __init__(self, Count ):
        self.Count = Count
    def GiveCount(self):
        return self.Count

Roomcount = RoomCount(3)
print(Roomcount.GiveCount())







# Building MCQs Game

questions_details = [
    "What is my Name?\n(a) Sami\n(b) Kashan\n(c) Ben\n\n",
    "What is my Qualification?\n(a) Bachelors in Software Engineering\n(b) Bachelors in Economics\n(c) Masters in FinTech\n\n",
    "How old I am??\n(a) Nineteen years old\n(b) Twenty One years old\n(c) Eighteen years old\n\n"
]

questions = [
    Question(questions_details[0], "b"),
    Question(questions_details[1], "a"),
    Question(questions_details[2], "b")
]

def run_test(questions):
    Score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            Score += 1
    print("You Scored " + str(Score) + "/" + str(len(questions)) + " Points")

run_test(questions)