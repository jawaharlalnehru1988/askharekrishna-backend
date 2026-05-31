"""
MCQ generation from OpenAI for Pooja Vidhi articles.
Returns a list of exactly 10 questions, each with 4 options.
"""
from mcq_shared import generate_mcqs as shared_generate_mcqs
from mcq_shared import save_mcqs as shared_save_mcqs


def generate_mcqs(article_text: str, language: str = "en") -> list:
    return shared_generate_mcqs(article_text, language=language)


def save_mcqs(pooja_vidhi, questions: list) -> int:
    from .models import PoojaVidhiQuestion, PoojaVidhiQuestionOption

    return shared_save_mcqs(
        pooja_vidhi,
        questions,
        question_model=PoojaVidhiQuestion,
        option_model=PoojaVidhiQuestionOption,
        parent_field_name="pooja_vidhi",
        question_field_name="question_text",
    )
