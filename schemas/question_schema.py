from pydantic import BaseModel
from typing import List
from models.difficulty import Difficulty
from schemas.answer_schema import AnswerCreateSchema, AnswerResponseSchema


class QuestionCreateSchema(BaseModel):
    question: str
    answers: List[AnswerCreateSchema]
    correctAnswer: str
    difficulty: Difficulty


class QuestionResponseSchema(BaseModel):
    question: str
    answers: List[AnswerResponseSchema]
    correctAnswer: str
    difficulty: str


class QuestionListResponseSchema(BaseModel):
    question:str

class QuestionParticipateResponseSchema(BaseModel):
    question: str
    answers: List[AnswerResponseSchema]
    
    
    class Config:
        orm_mode = True
