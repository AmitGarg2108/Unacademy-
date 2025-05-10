from quizzes.models import Quiz, Question
from datetime import date

def create_class10_english_quiz():
    quiz, created = Quiz.objects.get_or_create(
        title="Class 10 English Quiz",
        date=date.today(),
        description="An English quiz for class 10 students covering grammar, vocabulary, and comprehension.",
        subject="english",
        class_level="10",
        duration=20
    )
    if created:
        questions_data = [
            {
                "question_text": "Choose the correct form: She _____ to school every day.",
                "option1": "go",
                "option2": "goes",
                "option3": "going",
                "option4": "gone",
                "correct_option": 2
            },
            {
                "question_text": "What is the synonym of 'happy'?",
                "option1": "Sad",
                "option2": "Angry",
                "option3": "Joyful",
                "option4": "Tired",
                "correct_option": 3
            },
            {
                "question_text": "Fill in the blank: He is _____ than his brother.",
                "option1": "tall",
                "option2": "taller",
                "option3": "tallest",
                "option4": "more tall",
                "correct_option": 2
            },
            {
                "question_text": "Identify the adjective in the sentence: The quick brown fox jumps over the lazy dog.",
                "option1": "fox",
                "option2": "quick",
                "option3": "jumps",
                "option4": "dog",
                "correct_option": 2
            },
            {
                "question_text": "Choose the correct preposition: She is good _____ math.",
                "option1": "in",
                "option2": "at",
                "option3": "on",
                "option4": "for",
                "correct_option": 2
            },
            {
                "question_text": "What is the antonym of 'difficult'?",
                "option1": "Easy",
                "option2": "Hard",
                "option3": "Tough",
                "option4": "Complex",
                "correct_option": 1
            },
            {
                "question_text": "Choose the correct sentence:",
                "option1": "He don't like apples.",
                "option2": "He doesn't likes apples.",
                "option3": "He doesn't like apples.",
                "option4": "He don't likes apples.",
                "correct_option": 3
            },
            {
                "question_text": "Fill in the blank: They have been friends _____ childhood.",
                "option1": "since",
                "option2": "for",
                "option3": "from",
                "option4": "by",
                "correct_option": 1
            },
            {
                "question_text": "What is the plural form of 'child'?",
                "option1": "Childs",
                "option2": "Children",
                "option3": "Childes",
                "option4": "Child",
                "correct_option": 2
            },
            {
                "question_text": "Choose the correct past tense of 'go':",
                "option1": "goed",
                "option2": "went",
                "option3": "gone",
                "option4": "going",
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
        print("Class 10 English Quiz created with 10 questions.")
    else:
        print("Class 10 English Quiz already exists.")

if __name__ == "__main__":
    create_class10_english_quiz()
