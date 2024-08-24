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
    path('softwareeng/', views.softwareeng, name='softwareeng'),
    path('cybersec/', views.cybersec, name='cybersec'),
    path('webdev/', views.webdev, name='webdev'),
    path('networkeng/', views.networkeng, name='networkeng'),
    path('datasci/', views.datasci, name='datasci'),
    path('dba/', views.dba, name='dba'),
    path('lmobdev/', views.mobdev, name='mobdev'),
    path('compprog/', views.compprog, name='compprog'),
    path('netadm/', views.netadm, name='netadm'),
    path('cloudcompute/', views.cloudcompute, name='cloudcompute'),
    path('prodmaneg/', views.prodmaneg, name='prodmaneg'),
    path('ai/', views.ai, name='ai'),
    path('ba/', views.ba, name='ba'),
    path('testing/', views.testing, name='testing'),
    path('resume/', views.resume, name='resume'),
    path('linkedin/', views.linkedin, name='linkedin'),
    path('jobfind/', views.jobfind, name='jobfind'),
    path('contact/', views.contact, name='contact'),





    



]
