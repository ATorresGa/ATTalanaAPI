from pydantic import BaseModel

class RankingSchema(BaseModel):
    triviaId: int
    email: str
    score: int

class GetRankingSchema(BaseModel):
    triviaId: int