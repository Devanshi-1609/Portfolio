from django.contrib import admin

from .models import (
    Project,
    Contact,
    Profile,
    Skill,
    Milestone,
    Design
)


# PROFILE
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'profession',
        'email'
    )


# SKILLS
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'name',
        'percentage'
    )

    ordering = ['order']


# MILESTONES
@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'title',
        'date'
    )

    ordering = ['order']


# PROJECTS
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'title',
        'created_at'
    )

    ordering = ['order']


# CONTACTS
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'subject',
        'created_at'
    )

    readonly_fields = (
        'name',
        'email',
        'subject',
        'message',
        'created_at'
    )

    ordering = ['-created_at']


# DESIGNS
@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'title',
        'created_at'
    )

    ordering = ['order']