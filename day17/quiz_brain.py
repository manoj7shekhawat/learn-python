#!/usr/bin/env python3

class QuizBrain:

    def __init__(self, quesBank):
        self.quesNo = 0
        self.myscore = 0
        self.quesBank = quesBank


    def askQuestion(self):
        num = self.quesNo
        ans = input(f"Q{num + 1}: {self.quesBank[num].question}? (True/False): ")
        self.quesNo += 1
        self.checkAnswer(ans,num)


    def checkAnswer(self, ans, num):
        if ans == self.quesBank[num].correct_answer:
            self.myscore += 1
            print(f"You are right. Your score: {self.myscore}/{num + 1}")
        else:
            print(f"Wrong answer. Your score: {self.myscore}/{num + 1}")