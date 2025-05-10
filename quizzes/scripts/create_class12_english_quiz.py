from quizzes.models import Quiz, Question
from datetime import date

def create_class12_english_quiz():
    quiz, created = Quiz.objects.get_or_create(
        title="Class 12 English Quiz",
        date=date.today(),
        description="An English quiz for class 12 students covering grammar, vocabulary, and comprehension.",
        subject="english",
        class_level="12",
        duration=20
    )
    if created:
        questions_data = [
            {
                "question_text": "Choose the correct sentence:",
                "option1": "He don't like apples.",
                "option2": "He doesn't likes apples.",
                "option3": "He doesn't like apples.",
                "option4": "He don't likes apples.",
                "correct_option": 3
            },
            {
                "question_text": "What is the synonym of 'diligent'?",
                "option1": "Lazy",
                "option2": "Hardworking",
                "option3": "Careless",
                "option4": "Slow",
                "correct_option": 2
            },
            {
                "question_text": "Fill in the blank: She has been working here _____ 2010.",
                "option1": "since",
                "option2": "for",
                "option3": "from",
                "option4": "by",
                "correct_option": 1
            },
            {
                "question_text": "Identify the adverb in the sentence: He runs quickly.",
                "option1": "He",
                "option2": "runs",
                "option3": "quickly",
                "option4": "None",
                "correct_option": 3
            },
            {
                "question_text": "Choose the correct preposition: The book is _____ the table.",
                "option1": "on",
                "option2": "in",
                "option3": "at",
                "option4": "by",
                "correct_option": 1
            },
            {
                "question_text": "What is the antonym of 'generous'?",
                "option1": "Kind",
                "option2": "Selfish",
                "option3": "Helpful",
                "option4": "Friendly",
                "correct_option": 2
            },
            {
                "question_text": "Choose the correct past tense of 'write':",
                "option1": "writed",
                "option2": "wrote",
                "option3": "written",
                "option4": "writing",
                "correct_option": 2
            },
            {
                "question_text": "Fill in the blank: They _____ finished their homework.",
                "option1": "has",
                "option2": "have",
                "option3": "had",
                "option4": "having",
                "correct_option": 2
            },
            {
                "question_text": "What is the plural form of 'mouse'?",
                "option1": "mouses",
                "option2": "mice",
                "option3": "mouse",
                "option4": "meese",
                "correct_option": 2
            },
            {
                "question_text": "Choose the correct sentence:",
                "option1": "She can sings well.",
                "option2": "She can sing well.",
                "option3": "She can singing well.",
                "option4": "She can sang well.",
                "correct_option": 2
            }
        ]
        for q in questions_data:
            Question.objects.create(
                quiz=quiz,
                question_text=q["question_text"],
                option1=q["option1"],
                option2=q["option2"],
                option3=q["option3"],
                option4=q["option4"],
                correct_option=q["correct_option"]
            )
        print("Class 12 English Quiz created with 10 questions.")
    else:
        print("Class 12 English Quiz already exists.")

if __name__ == "__main__":
    create_class12_english_quiz()
