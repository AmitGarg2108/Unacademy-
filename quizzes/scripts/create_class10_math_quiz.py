from quizzes.models import Quiz, Question
from datetime import date

def create_class10_math_quiz():
    quiz, created = Quiz.objects.get_or_create(
        title="Class 10 Math Quiz",
        date=date.today(),
        description="A math quiz for class 10 students covering algebra, geometry, and arithmetic.",
        subject="math",
        class_level="10",
        duration=20
    )
    if created:
        questions_data = [
            {
                "question_text": "What is the value of \\(x\\) if \\(2x + 3 = 7\\)?",
                "option1": "1",
                "option2": "2",
                "option3": "3",
                "option4": "4",
                "correct_option": 2
            },
            {
                "question_text": "What is the area of a triangle with base 5 and height 8?",
                "option1": "20",
                "option2": "40",
                "option3": "13",
                "option4": "10",
                "correct_option": 1
            },
            {
                "question_text": "What is the square root of 144?",
                "option1": "10",
                "option2": "11",
                "option3": "12",
                "option4": "13",
                "correct_option": 3
            },
            {
                "question_text": "What is the next prime number after 7?",
                "option1": "9",
                "option2": "11",
                "option3": "13",
                "option4": "15",
                "correct_option": 2
            },
            {
                "question_text": "What is the value of \\(7 \\times 6\\)?",
                "option1": "42",
                "option2": "36",
                "option3": "48",
                "option4": "40",
                "correct_option": 1
            },
            {
                "question_text": "What is the perimeter of a square with side length 4?",
                "option1": "12",
                "option2": "16",
                "option3": "20",
                "option4": "8",
                "correct_option": 2
            },
            {
                "question_text": "What is the value of \\(3^3\\)?",
                "option1": "6",
                "option2": "9",
                "option3": "27",
                "option4": "81",
                "correct_option": 3
            },
            {
                "question_text": "What is the sum of angles in a triangle?",
                "option1": "90 degrees",
                "option2": "180 degrees",
                "option3": "270 degrees",
                "option4": "360 degrees",
                "correct_option": 2
            },
            {
                "question_text": "What is the value of \\(\\frac{1}{2} + \\frac{1}{3}\\)?",
                "option1": "\\(\\frac{2}{5}\\)",
                "option2": "\\(\\frac{3}{5}\\)",
                "option3": "\\(\\frac{5}{6}\\)",
                "option4": "\\(\\frac{1}{6}\\)",
                "correct_option": 3
            },
            {
                "question_text": "What is the value of \\(10^0\\)?",
                "option1": "0",
                "option2": "1",
                "option3": "10",
                "option4": "Undefined",
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
        print("Class 10 Math Quiz created with 10 questions.")
    else:
        print("Class 10 Math Quiz already exists.")

if __name__ == "__main__":
    create_class10_math_quiz()
