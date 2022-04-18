class Quiz_Brain:
    def __init__(self,question_bank) :
        self.question_number=0
        self.question_list=question_bank
        self.score=0
    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number+=1
        user_ans=input(f"Q.{self.question_number}: {question.text} (True/False): \n")
        self.check_answer(user_ans,question.answer)
    def still_has_questions(self):
        return self.question_number<(len(self.question_list))
    def check_answer(self,u_ans,c_ans):
        print("\n")
        if u_ans.lower()==c_ans.lower():
            print("you got it right!!")
            self.score+=1    
        else:
            print("Oops!! Thats wrong!!")
            print(f"The correct answer is:{c_ans}")
        print(f"your current Score is: {self.score}/{self.question_number}")
   
    

