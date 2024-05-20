from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ProjectForm, EducationForm, WorkExperienceForm, CertificationForm
from .models import Project, Education, WorkExperience, Certification

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profiles/edit_profile.html', {'form': form})

@login_required
def profile(request):
    user_profile = request.user.userprofile
    projects = Project.objects.filter(user_profile=user_profile)
    education = Education.objects.filter(user_profile=user_profile)
    work_experience = WorkExperience.objects.filter(user_profile=user_profile)
    certifications = Certification.objects.filter(user_profile=user_profile)
    context = {
        'user_profile': user_profile,
        'projects': projects,
        'education': education,
        'work_experience': work_experience,
        'certifications': certifications
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user_profile = request.user.userprofile
            project.save()
            return redirect('profile')
    else:
        form = ProjectForm()
    return render(request, 'profiles/add_project.html', {'form': form})

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'profiles/project_detail.html', {'project': project})

@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user_profile = request.user.userprofile
            education.save()
            return redirect('profile')
    else:
        form = EducationForm()
    return render(request, 'profiles/add_education.html', {'form': form})

@login_required
def add_work_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.user_profile = request.user.userprofile
            work_experience.save()
            return redirect('profile')
    else:
        form = WorkExperienceForm()
    return render(request, 'profiles/add_work_experience.html', {'form': form})

@login_required
def add_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user_profile = request.user.userprofile
            certification.save()
            return redirect('profile')
    else:
        form = CertificationForm()
    return render(request, 'profiles/add_certification.html', {'form': form})

