from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain
question_bank=[]
for dict in question_data:
    new_quest=Question(dict["text"],answer=dict["answer"])
    question_bank.append(new_quest)

quiz=Quiz_Brain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("Congrats!!You've completed the quiz")
print(f"Your final score : {quiz.score}/{len(question_bank)}")
