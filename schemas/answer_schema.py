from pydantic import BaseModel

class AnswerCreateSchema(BaseModel):
    answer: str
    
class AnswerResponseSchema(BaseModel):
    answer: str


    class Config:
        orm_mode = True
