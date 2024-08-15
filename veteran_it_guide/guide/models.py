# models.py
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coding_languages = models.TextField(blank=True)  # Consider changing to CharField if it's a single language or ManyToManyField for multiple
    tech_career_interest = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

# Admin interface registration
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'coding_languages', 'tech_career_interest')

admin.site.register(UserProfile, UserProfileAdmin)
