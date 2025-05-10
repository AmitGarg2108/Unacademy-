from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import StudyMaterial
from .forms import StudyMaterialForm

@login_required
def study_materials_view(request):
    class_name = request.GET.get('class_name', '')
    entrance_exam = request.GET.get('entrance_exam', '')

    materials = StudyMaterial.objects.all()
    if class_name:
        materials = materials.filter(class_name=class_name)
    if entrance_exam:
        materials = materials.filter(entrance_exam=entrance_exam)

    return render(request, 'materials/study_materials.html', {'materials': materials})

@login_required
def upload_study_material_view(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('study_materials')
    else:
        form = StudyMaterialForm()
    return render(request, 'materials/upload_study_material.html', {'form': form})

@login_required
def view_study_material(request, pk):
    material = StudyMaterial.objects.get(pk=pk)
    return render(request, 'materials/view_study_material.html', {'material': material})
