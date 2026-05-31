"""
MCQ generation from OpenAI for Debate articles.
Returns a list of exactly 10 questions, each with 4 options.
"""
from mcq_shared import generate_mcqs as shared_generate_mcqs
from mcq_shared import save_mcqs as shared_save_mcqs


def generate_mcqs(article_text: str, language: str = "en") -> list:
    return shared_generate_mcqs(
        article_text,
        language=language,
    )


def save_mcqs(debate_article, questions: list) -> int:
    from .models import DebateQuestion, DebateQuestionOption

    return shared_save_mcqs(
        debate_article,
        questions,
        question_model=DebateQuestion,
        option_model=DebateQuestionOption,
        parent_field_name="debate_article",
        question_field_name="question_text",
    )
