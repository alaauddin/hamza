from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, SkillCategory, Experience, Education, Project, Message

def home(request):
    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    projects = Project.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_body = request.POST.get('message')

        if name and email and subject and message_body:
            Message.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message_body
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')

    context = {
        'profile': profile,
        'skill_categories': skill_categories,
        'experiences': experiences,
        'educations': educations,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)
