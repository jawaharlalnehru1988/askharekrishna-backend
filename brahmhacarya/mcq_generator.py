"""
MCQ generation from OpenAI for Brahmhacarya articles.
Returns a list of exactly 10 questions, each with 4 options.
"""
from mcq_shared import generate_mcqs as shared_generate_mcqs
from mcq_shared import save_mcqs as shared_save_mcqs


def generate_mcqs(article_text: str, language: str = "en") -> list:
    return shared_generate_mcqs(
        article_text,
        language=language,
        extra_rules="- Focus the questions on principles, teachings, values, lessons, and philosophy from the article.",
    )


def save_mcqs(article, questions: list) -> int:
    from .models import BrahmhacaryaQuestion, BrahmhacaryaQuestionOption

    return shared_save_mcqs(
        article,
        questions,
        question_model=BrahmhacaryaQuestion,
        option_model=BrahmhacaryaQuestionOption,
        parent_field_name="article",
        question_field_name="question_text",
    )
