from models.answer import Answer
from typing import List

from models.difficulty import Difficulty

class Question():
    def __init__(self, question:str, answers: List[Answer], correctAnswer: str, difficulty:Difficulty):
        self.question = question
        self.answers = answers
        self.correctAnswer= correctAnswer
        self.difficulty = difficulty     