import os
import sys
import shutil
import django

# Add parent directory to sys.path for Django import
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unacademy_website.settings')
django.setup()

from materials.models import StudyMaterial
from django.core.files import File

# Paths
project_root = parent_dir
source_pdf_path = os.path.join(project_root, '12th_Physics_EngMed_QueBank_MSCERT.pdf')
media_dir = os.path.join(project_root, 'media', 'study_materials')
os.makedirs(media_dir, exist_ok=True)
dest_pdf_path = os.path.join(media_dir, '12th_Physics_EngMed_QueBank_MSCERT.pdf')

# Move the PDF file to media/study_materials/
if not os.path.exists(dest_pdf_path):
    shutil.move(source_pdf_path, dest_pdf_path)
    print(f"Moved PDF to {dest_pdf_path}")
else:
    print(f"PDF already exists at {dest_pdf_path}")

# Create StudyMaterial instance
from django.core.files.base import ContentFile

with open(dest_pdf_path, 'rb') as f:
    file_content = ContentFile(f.read())
    sm, created = StudyMaterial.objects.get_or_create(
        title='12th Physics EngMed QueBank MSCERT',
        defaults={
            'class_name': '12',
            'entrance_exam': '',
        }
    )
    if created:
        sm.file.save('12th_Physics_EngMed_QueBank_MSCERT.pdf', file_content, save=True)
        print("StudyMaterial instance created and file saved.")
    else:
        print("StudyMaterial instance already exists.")
