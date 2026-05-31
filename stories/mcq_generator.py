"""
MCQ generation from OpenAI for Stories.
Returns a list of exactly 10 questions, each with 4 options.
"""
from mcq_shared import generate_mcqs as shared_generate_mcqs
from mcq_shared import save_mcqs as shared_save_mcqs


def generate_mcqs(article_text: str, language: str = "en") -> list:
    return shared_generate_mcqs(
        article_text,
        language=language,
        extra_rules=(
            "- Focus the questions on principles, teachings, values, lessons, and philosophy from the article.\n"
            "- Avoid questions that mainly test memory of character names, identity, or minor story details.\n"
            "- Use characters or events only when needed to test the underlying principle or philosophical point."
        ),
    )


def save_mcqs(story, questions: list) -> int:
    from .models import StoryQuestion, StoryQuestionOption

    return shared_save_mcqs(
        story,
        questions,
        question_model=StoryQuestion,
        option_model=StoryQuestionOption,
        parent_field_name="story",
        question_field_name="question_text",
    )
