from quizzes.models import Quiz, Question
from datetime import date

def create_class12_math_quiz():
    quiz, created = Quiz.objects.get_or_create(
        title="Class 12 Math Quiz",
        date=date.today(),
        description="A math quiz for class 12 students covering calculus, algebra, and geometry.",
        subject="math",
        class_level="12",
        duration=20
    )
    if created:
        questions_data = [
            {
                "question_text": "What is the derivative of \\(x^2\\)?",
                "option1": "2x",
                "option2": "x",
                "option3": "x^2",
                "option4": "1",
                "correct_option": 1
            },
            {
                "question_text": "What is the integral of \\(2x\\)?",
                "option1": "x^2 + C",
                "option2": "2x + C",
                "option3": "x + C",
                "option4": "1 + C",
                "correct_option": 1
            },
            {
                "question_text": "What is the solution to the equation \\(x^2 - 4 = 0\\)?",
                "option1": "x = 2",
                "option2": "x = -2",
                "option3": "x = 2 or x = -2",
                "option4": "x = 0",
                "correct_option": 3
            },
            {
                "question_text": "What is the value of \\(\\sin 90^\\circ\\)?",
                "option1": "0",
                "option2": "1",
                "option3": "0.5",
                "option4": "-1",
                "correct_option": 2
            },
            {
                "question_text": "What is the sum of the interior angles of a triangle?",
                "option1": "180 degrees",
                "option2": "90 degrees",
                "option3": "360 degrees",
                "option4": "270 degrees",
                "correct_option": 1
            },
            {
                "question_text": "What is the quadratic formula?",
                "option1": "\\(\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}\\)",
                "option2": "\\(\\frac{-b \\pm \\sqrt{4ac - b^2}}{2a}\\)",
                "option3": "\\(\\frac{b \\pm \\sqrt{b^2 - 4ac}}{2a}\\)",
                "option4": "\\(\\frac{-b \\pm \\sqrt{b^2 + 4ac}}{2a}\\)",
                "correct_option": 1
            },
            {
                "question_text": "What is the value of \\(\\log 100\\) (base 10)?",
                "option1": "1",
                "option2": "2",
                "option3": "10",
                "option4": "100",
                "correct_option": 2
            },
            {
                "question_text": "What is the formula for the area of a circle?",
                "option1": "\\(\\pi r^2\\)",
                "option2": "\\(2\\pi r\\)",
                "option3": "\\(\\pi d\\)",
                "option4": "\\(\\frac{1}{2} \\pi r^2\\)",
                "correct_option": 1
            },
            {
                "question_text": "What is the value of \\(e\\) (Euler's number) approximately?",
                "option1": "2.718",
                "option2": "3.141",
                "option3": "1.618",
                "option4": "1.414",
                "correct_option": 1
            },
            {
                "question_text": "What is the solution to the system of equations: \\(x + y = 5\\) and \\(x - y = 1\\)?",
                "option1": "\\(x=3, y=2\\)",
                "option2": "\\(x=2, y=3\\)",
                "option3": "\\(x=4, y=1\\)",
                "option4": "\\(x=1, y=4\\)",
                "correct_option": 1
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
        print("Class 12 Math Quiz created with 10 questions.")
    else:
        print("Class 12 Math Quiz already exists.")

if __name__ == "__main__":
    create_class12_math_quiz()
