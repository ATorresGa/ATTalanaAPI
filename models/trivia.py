from typing import List
from models.question import Question

class Trivia:
    def __init__(self, id:int, name:str, description:str, questions:List[Question]):
        self.id = id
        self.name = name
        self.description = description
        self.questions= questions
