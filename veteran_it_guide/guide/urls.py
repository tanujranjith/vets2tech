from django.urls import path
from . import views
from .views import additional_info
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),  # This should match the view function name
    path('employment/', views.employment, name='employment'),
    path('donate/', views.donate, name='donate'),
    path('profile/', views.profile, name='profile'),
    path('chat/', views.chat, name='chat'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('additional-info/', views.additional_info, name='additional_info'),
    path('success/', views.success_view, name='success'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('edit-preferences/', views.edit_preferences, name='edit_preferences'),
    path('courses/', views.view_courses, name='view_courses'),
    path('profile-view/', views.profile_view, name='profile_view'),
]
