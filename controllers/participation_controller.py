from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from schemas.ranking_schema import RankingSchema
from schemas.trivia_schema import TriviaUserParticipationSchema
from services.trivia_service import get_trivia_by_id
from services.user_service import get_user_by_id
from services.participation_service import calculate_questions_score
from services.ranking_service import create_ranking


participation_blueprint = Blueprint("participation", __name__)

@participation_blueprint.route("/participate/", methods = ["POST"])
def user_participate_trivia_ep():
    try:
        data = request.get_json()
        userParticipationSchema = TriviaUserParticipationSchema(**data)
        userId = userParticipationSchema.userId
        answers = userParticipationSchema.answers

        user = get_user_by_id(userId)
        trivia = get_trivia_by_id(user.triviaId)
        score = calculate_questions_score(trivia.questions,answers)

        ranking = create_ranking(trivia, user.email, score)
        return jsonify(RankingSchema(triviaId= ranking.triviaId, email= ranking.email, score= ranking.score).model_dump()),201

    except ValidationError as e:
        return jsonify({"error": str(e)}), 400