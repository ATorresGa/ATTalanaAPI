from pydantic import BaseModel
from typing import List
from schemas.question_schema import QuestionCreateSchema, QuestionResponseSchema, QuestionListResponseSchema, QuestionParticipateResponseSchema
from schemas.answer_schema import AnswerResponseSchema

class TriviaCreateSchema(BaseModel):
    name: str
    description: str
    questions: List[QuestionCreateSchema]

class TriviaResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    questions: List[QuestionResponseSchema]

class TriviaListSchema(BaseModel):
    id:int

class TriviaResponseListSchema(BaseModel):
    id:int
    name:str
    description:str
    questions: List[QuestionListResponseSchema]

class TriviaParticipateResponseSchema(BaseModel):
    id: int
    name: str
    description: str
    questions: List[QuestionParticipateResponseSchema]

class TriviaUserParticipationSchema(BaseModel):
    userId: int
    answers: List[AnswerResponseSchema]
    
    class Config:
        orm_mode = True
