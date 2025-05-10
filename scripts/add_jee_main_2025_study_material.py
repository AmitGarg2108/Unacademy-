import os
import sys
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unacademy_website.settings')
django.setup()

from materials.models import StudyMaterial

def add_jee_main_2025_study_material():
    file_path = 'study_materials/13629-JEE-Main-2025-Question-Paper-with-Solution-22-Jan-Shift-1-PDF.pdf'
    title = 'JEE Main 2025 Question Paper with Solution - 22 Jan Shift 1'

    # Check if the StudyMaterial already exists
    if StudyMaterial.objects.filter(title=title).exists():
        print(f'StudyMaterial "{title}" already exists.')
        return

    # Create new StudyMaterial entry
    material = StudyMaterial(title=title, file=file_path)
    material.save()
    print(f'StudyMaterial "{title}" added successfully.')

if __name__ == '__main__':
    add_jee_main_2025_study_material()
