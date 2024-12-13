from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from schemas.answer_schema import AnswerResponseSchema
from schemas.question_schema import QuestionResponseSchema, QuestionListResponseSchema
from schemas.trivia_schema import TriviaCreateSchema, TriviaResponseSchema, TriviaListSchema, TriviaResponseListSchema
from services.trivia_service import create_trivia, get_trivia_and_questions

trivia_blueprint = Blueprint("trivia", __name__)

@trivia_blueprint.route("/trivia/", methods = ["POST"])
def create_trivia_ep():
    try:
        data = request.get_json()
        triviaSchema = TriviaCreateSchema(**data)
        createdTrivia = create_trivia(triviaSchema.name, triviaSchema.description,
                                       triviaSchema.questions)
        
        transformed_questions = [
            QuestionResponseSchema(
            question=q.question,
            answers=[AnswerResponseSchema(answer = a.answer) for a in q.answers],
            correctAnswer=q.correctAnswer,
            difficulty= q.difficulty.value
            )
                for q in createdTrivia.questions
        ]
        return jsonify (TriviaResponseSchema(id=createdTrivia.id, name=createdTrivia.name, description=createdTrivia.description,
                                              questions=transformed_questions).model_dump()), 201
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400    
    
@trivia_blueprint.route("/get-questions-by-trivia/", methods = ["GET"])
def get_trivia_questions_ep():
    try:
        data = request.get_json()
        triviaListSchema = TriviaListSchema(**data)
        triviaId = triviaListSchema.id
        triviaQuestionList = get_trivia_and_questions(triviaId)
        transformedQuestions = [
            QuestionListResponseSchema(
                question=q.question
            )
                for q in triviaQuestionList.questions
        ]
        return jsonify(TriviaResponseListSchema(id=triviaQuestionList.id, name=triviaQuestionList.name, description= triviaQuestionList.description, questions= transformedQuestions).model_dump()), 200
    except ValidationError as e:
        return jsonify({"error":str(e)}), 400    