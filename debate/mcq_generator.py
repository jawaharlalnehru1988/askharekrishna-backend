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


def save_mcqs(debate_article, questions: list, language: str = "en") -> int:
    from .models import DebateQuestion, DebateQuestionOption

    # Delete existing questions for this specific language
    debate_article.questions.filter(language=language).delete()

    for q_data in questions:
        question = DebateQuestion.objects.create(
            debate_article=debate_article,
            language=language,
            question_text=q_data["question"],
            order=q_data["order"],
            is_active=True,
        )
        for opt in q_data["options"]:
            DebateQuestionOption.objects.create(
                question=question,
                option_text=opt["text"],
                order=opt["order"],
                is_correct=opt["is_correct"],
            )

    return len(questions)
