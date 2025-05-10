from quizzes.models import Quiz, Question
from datetime import date

def create_class12_science_quiz():
    quiz, created = Quiz.objects.get_or_create(
        title="Class 12 Science Quiz",
        date=date.today(),
        description="A science quiz for class 12 students covering physics, chemistry, and biology.",
        subject="science",
        class_level="12",
        duration=20
    )
    if created:
        questions_data = [
            {
                "question_text": "What is the chemical symbol for Sodium?",
                "option1": "Na",
                "option2": "S",
                "option3": "So",
                "option4": "N",
                "correct_option": 1
            },
            {
                "question_text": "What is the unit of electric resistance?",
                "option1": "Ohm",
                "option2": "Volt",
                "option3": "Ampere",
                "option4": "Watt",
                "correct_option": 1
            },
            {
                "question_text": "Which gas is used in the Haber process?",
                "option1": "Oxygen",
                "option2": "Nitrogen",
                "option3": "Hydrogen",
                "option4": "Ammonia",
                "correct_option": 2
            },
            {
                "question_text": "What is the pH of a neutral solution?",
                "option1": "0",
                "option2": "7",
                "option3": "14",
                "option4": "1",
                "correct_option": 2
            },
            {
                "question_text": "What is the speed of sound in air?",
                "option1": "343 m/s",
                "option2": "300 m/s",
                "option3": "150 m/s",
                "option4": "500 m/s",
                "correct_option": 1
            },
            {
                "question_text": "Which part of the cell contains genetic material?",
                "option1": "Cytoplasm",
                "option2": "Nucleus",
                "option3": "Cell membrane",
                "option4": "Mitochondria",
                "correct_option": 2
            },
            {
                "question_text": "What is the formula for force?",
                "option1": "Mass x Acceleration",
                "option2": "Mass / Acceleration",
                "option3": "Mass + Acceleration",
                "option4": "Mass - Acceleration",
                "correct_option": 1
            },
            {
                "question_text": "What is the chemical formula of sulfuric acid?",
                "option1": "H2SO4",
                "option2": "HCl",
                "option3": "NaOH",
                "option4": "HNO3",
                "correct_option": 1
            },
            {
                "question_text": "Which vitamin is produced when skin is exposed to sunlight?",
                "option1": "Vitamin A",
                "option2": "Vitamin B",
                "option3": "Vitamin C",
                "option4": "Vitamin D",
                "correct_option": 4
            },
            {
                "question_text": "What is the process of cell division in somatic cells called?",
                "option1": "Meiosis",
                "option2": "Mitosis",
                "option3": "Fission",
                "option4": "Fusion",
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
        print("Class 12 Science Quiz created with 10 questions.")
    else:
        print("Class 12 Science Quiz already exists.")

if __name__ == "__main__":
    create_class12_science_quiz()
