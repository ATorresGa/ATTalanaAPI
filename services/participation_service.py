from models.question import Question
from models.answer import Answer
from typing import List
from utils.constans import CORRECT_ANSWER_MEDIUM_SCORE, CORRECT_ANSWER_EASY_SCORE, CORRECT_ANSWER_HARD_SCORE

def is_valid_answer(answers: List[Answer], userAnswer: str) -> bool:
    return userAnswer in answers

def calculate_questions_score(questions: List[Question], userAnswers: List[str]) -> int:
    user_answers = [answer.answer for answer in userAnswers]
    score = 0
    
    for question, userAnswer in zip(questions, user_answers):
        if userAnswer.strip().lower() == question.correctAnswer.strip().lower():
            if question.difficulty.value == "Easy":
                score = score+CORRECT_ANSWER_EASY_SCORE
            elif question.difficulty.value == "Medium":
                score = score+CORRECT_ANSWER_MEDIUM_SCORE
            elif question.difficulty.value == "Hard":
                score = score+CORRECT_ANSWER_HARD_SCORE
    return score

    
