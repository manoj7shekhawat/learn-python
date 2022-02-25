#!/usr/bin/env python3

# Simple HTTP module
import requests

# Simple JSON module
import json

from question_model import Question
from quiz_brain import QuizBrain

# https://opentdb.com/
num_of_questions = int(input("How many questions you need: "))
r = requests.get(f"https://opentdb.com/api.php?type=boolean&amount={num_of_questions}")

if r.status_code == 200:
    result = json.loads(r.text)

question_bank = []
# Build question bank
for x in result["results"]:
    question = Question(x["question"], x["correct_answer"])
    question_bank.append(question)

qb = QuizBrain(question_bank)
counter = 0

while counter < len(question_bank):
    qb.askQuestion()
    counter += 1

print(f"You final score {qb.myscore}/{counter}")


