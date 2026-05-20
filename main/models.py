from django.db import models


# PROFILE MODEL
class Profile(models.Model):

    name = models.CharField(max_length=200)

    profession = models.CharField(max_length=300)

    about_image = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    short_bio = models.TextField()

    phone = models.CharField(max_length=100)

    location = models.CharField(max_length=300)

    resume = models.FileField(upload_to='resume/')

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    instagram = models.URLField(blank=True)

    email = models.EmailField()

    footer_description = models.TextField()

    projects_completed = models.IntegerField(default=0)

    years_experience = models.IntegerField(default=0)

    technologies_used = models.IntegerField(default=0)

    def __str__(self):

        return self.name


# SKILLS MODEL
class Skill(models.Model):

    order = models.IntegerField(default=0)

    name = models.CharField(max_length=200)

    percentage = models.IntegerField()

    def __str__(self):

        return self.name


# MILESTONES MODEL
class Milestone(models.Model):

    order = models.IntegerField(default=0)

    date = models.CharField(max_length=100)

    title = models.CharField(max_length=200)

    subtitle = models.CharField(max_length=300)

    description = models.TextField()

    def __str__(self):

        return self.title


# PROJECT MODEL
class Project(models.Model):

    order = models.IntegerField(default=0)

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='projects/')

    technologies = models.CharField(max_length=300)

    source_code = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


# CONTACT MODEL
class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name


# DESIGN MODEL
class Design(models.Model):

    order = models.IntegerField(default=0)

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='designs/')

    tools_used = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title