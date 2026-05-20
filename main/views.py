from django.shortcuts import render, redirect

from django.core.mail import send_mail

from .models import (
    Milestone,
    Profile,
    Project,
    Contact,
    Skill,
    Design
)


# HOME PAGE
def home(request):

    profile = Profile.objects.first()

    featured_projects = Project.objects.all().order_by('order')[:3]

    return render(
        request,
        'index.html',
        {
            'profile': profile,
            'featured_projects': featured_projects
        }
    )


# ABOUT PAGE
def about(request):

    profile = Profile.objects.first()

    skills = Skill.objects.all().order_by('order')

    milestones = Milestone.objects.all().order_by('order')

    return render(
        request,
        'about.html',
        {
            'profile': profile,
            'skills': skills,
            'milestones': milestones
        }
    )


# PROJECTS PAGE
def projects(request):

    profile = Profile.objects.first()

    projects = Project.objects.all().order_by('order')

    return render(
        request,
        'projects.html',
        {
            'profile': profile,
            'projects': projects
        }
    )


# DESIGNS PAGE
def designs(request):

    profile = Profile.objects.first()

    designs = Design.objects.all().order_by('order')

    return render(
        request,
        'design.html',
        {
            'profile': profile,
            'designs': designs
        }
    )


# CONTACT PAGE
def contact(request):

    profile = Profile.objects.last()

    if request.method == 'POST':

        name = request.POST.get('name')

        email = request.POST.get('email')

        subject = request.POST.get('subject')

        message = request.POST.get('message')

        # SAVE IN DATABASE
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # SEND EMAIL
        send_mail(

            subject=f'Portfolio Contact: {subject}',

            message=f'''
New Portfolio Contact Form Submission

Name: {name}

Email: {email}

Message:
{message}
''',

            from_email='YOUR_GMAIL@gmail.com',

            recipient_list=['devanshi1630@gmail.com'],

            fail_silently=False,
        )

        return redirect('/contact/')

    return render(
        request,
        'contact.html',
        {
            'profile': profile
        }
    )