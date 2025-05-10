from django.core.management.base import BaseCommand
from quizzes.models import Quiz, Question
from datetime import date

class Command(BaseCommand):
    help = 'Create Class 10 Science Quiz with 10 questions'

    def handle(self, *args, **kwargs):
        quiz, created = Quiz.objects.get_or_create(
            title="Class 10 Science Quiz",
            date=date.today(),
            description="A science quiz for class 10 students covering physics, chemistry, and biology.",
            subject="science",
            class_level="10",
            duration=20
        )
        if created:
            questions_data = [
                {
                    "question_text": "What is the chemical formula of water?",
                    "option1": "H2O",
                    "option2": "CO2",
                    "option3": "O2",
                    "option4": "NaCl",
                    "correct_option": 1
                },
                {
                    "question_text": "What is the unit of electric current?",
                    "option1": "Volt",
                    "option2": "Ampere",
                    "option3": "Ohm",
                    "option4": "Watt",
                    "correct_option": 2
                },
                {
                    "question_text": "Which gas is most abundant in the Earth's atmosphere?",
                    "option1": "Oxygen",
                    "option2": "Nitrogen",
                    "option3": "Carbon Dioxide",
                    "option4": "Hydrogen",
                    "correct_option": 2
                },
                {
                    "question_text": "What is the process by which plants make their food?",
                    "option1": "Respiration",
                    "option2": "Photosynthesis",
                    "option3": "Transpiration",
                    "option4": "Digestion",
                    "correct_option": 2
                },
                {
                    "question_text": "What is the speed of light?",
                    "option1": "3 x 10^8 m/s",
                    "option2": "3 x 10^6 m/s",
                    "option3": "3 x 10^5 m/s",
                    "option4": "3 x 10^7 m/s",
                    "correct_option": 1
                },
                {
                    "question_text": "Which element has the atomic number 1?",
                    "option1": "Helium",
                    "option2": "Hydrogen",
                    "option3": "Oxygen",
                    "option4": "Carbon",
                    "correct_option": 2
                },
                {
                    "question_text": "What is the SI unit of force?",
                    "option1": "Newton",
                    "option2": "Joule",
                    "option3": "Pascal",
                    "option4": "Watt",
                    "correct_option": 1
                },
                {
                    "question_text": "Which part of the plant conducts water?",
                    "option1": "Phloem",
                    "option2": "Xylem",
                    "option3": "Stomata",
                    "option4": "Chloroplast",
                    "correct_option": 2
                },
                {
                    "question_text": "What is the pH of pure water?",
                    "option1": "7",
                    "option2": "0",
                    "option3": "14",
                    "option4": "1",
                    "correct_option": 1
                },
                {
                    "question_text": "Which gas is released during photosynthesis?",
                    "option1": "Oxygen",
                    "option2": "Carbon Dioxide",
                    "option3": "Nitrogen",
                    "option4": "Hydrogen",
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
            self.stdout.write(self.style.SUCCESS("Class 10 Science Quiz created with 10 questions."))
        else:
            self.stdout.write("Class 10 Science Quiz already exists.")
