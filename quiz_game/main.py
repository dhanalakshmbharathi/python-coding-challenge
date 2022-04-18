from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain
question_bank=[]
for dict in question_data:
    new_quest=Question(dict["question"],answer=dict["correct_answer"])
    question_bank.append(new_quest)
def game():

    quiz=Quiz_Brain(question_bank)
    num=0

    while quiz.still_has_questions() and num<10:
        quiz.next_question()
        num+=1
    print("Congrats!!You've completed the quiz")
    print(f"Your final score : {quiz.score}/{len(question_bank)}")
game()
key=input("Want to start again?(yes/no)")
if key=="yes":
    game()