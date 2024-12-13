from models.trivia import Trivia
from models.question import Question
from models.answer import Answer
from typing import List, Optional
import sys


trivias: List[Trivia] = []

def is_valid_correct_answer(answers: List[Answer], correctAnswer:str)->bool:
    return correctAnswer in answers

def validate_questions(questions:List[Question])->bool:
    for question in questions:
        if not is_valid_correct_answer(question.answers, question.correctAnswer):
            return False
    return True

def create_trivia(name: str, description: str,questions: List[Question])->Trivia:
    if not validate_questions:
        raise ValueError('Una de tus preguntas no contiene la respusta correcta, intenta nuevamente')
    trivia_id = len(trivias)+1
    trivia = Trivia(trivia_id, name, description, questions)
    trivias.append(trivia)
    print(len(trivias), file=sys.stderr)

    return trivia

def get_trivia_and_questions(triviaId:int)-> Optional[Trivia]:
    return next((trivia for trivia in trivias if trivia.id == triviaId), None)

def get_trivia_by_id(triviaId: int) ->Optional[Trivia]:
    return next((trivia for trivia in trivias if trivia.id == triviaId), None)