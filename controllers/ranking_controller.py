from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from schemas.ranking_schema import RankingSchema, GetRankingSchema
from services.ranking_service import get_raking_by_trivia

ranking_blueprint = Blueprint("ranking", __name__)

@ranking_blueprint.route("/get_rank_by_trivia_id/", methods = ["POST"])
def get_rank_by_trivia_id_ep():
    try:
        data = request.get_json()
        rankingSchema = GetRankingSchema(**data)
        triviaId = rankingSchema.triviaId
        rankings = get_raking_by_trivia(triviaId)

        return jsonify([RankingSchema(triviaId=ranking.triviaId, email=ranking.email, score= ranking.score).model_dump() for ranking in rankings]), 200
    except ValidationError as e:
        return jsonify({"error":str(e)}), 400    