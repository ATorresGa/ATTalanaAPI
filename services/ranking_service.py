from models.ranking import Ranking
from models.trivia import Trivia
from typing import List, Optional

rankings: List[Ranking]=[]

def create_ranking (trivia: Trivia, email: str, score:int) -> Ranking:
    ranking = Ranking(trivia.id, email, score)
    rankings.append(ranking)
    return ranking

def get_rankings()-> List[Ranking]:
    return sorted(rankings, key = lambda r:r.score, reverse= True)

def get_my_rank(email:str) -> Optional[Ranking]:
    ##cambiar por get my ranks
    ranking = next((ranking for ranking in rankings if ranking.email == email), None)

    if ranking is None:
        raise ValueError(f"No hay ranking asociado al correo: {email}")
    
    return ranking

def get_raking_by_trivia(triviaId) -> Optional[List[Ranking]]:
    if len(rankings)<1:
        raise ValueError("Aun no hay rankings en esta trivia")
    filtered_rankings = [
        ranking for ranking in rankings if ranking.triviaId == triviaId
    ]
    sorted_rankings = sorted(filtered_rankings, key=lambda r: r.score, reverse=True)
    top_10_rankings = sorted_rankings[:10]
    return top_10_rankings
