import os
import google.generativeai as genai
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .forms import AdditionalInfoForm, EditProfileForm
from .models import UserProfile

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def education(request):
    response_text = None
    error_message = None

    try:
        user_profile = UserProfile.objects.get(user=request.user)
        coding_interests = user_profile.coding_languages or "Python, JavaScript"

        if request.method == 'POST':
            user_input = request.POST.get('user_input')

            if not user_input.strip():
                error_message = "Please enter a valid message."
            else:
                try:
                    api_key = os.getenv("GOOGLE_API_KEY")
                    if not api_key:
                        raise ValueError("API key is missing")

                    genai.configure(api_key=api_key)
                    generation_config = {
                        "temperature": 1,
                        "top_p": 0.95,
                        "top_k": 64,
                        "max_output_tokens": 8192,
                        "response_mime_type": "text/plain",
                    }
                    model = genai.GenerativeModel(
                        model_name="gemini-1.5-flash",
                        generation_config=generation_config,
                    )
                    chat_session = model.start_chat(
                        history=[
                            {
                                "role": "user",
                                "parts": [
                                    f"You are Sam, a friendly assistant who works for Veteran IT Guide. Suggest 10 courses based on the user's coding interests which are: {coding_interests}. The courses should be ordered from beginner to job readiness and include links also make sure to never use the symbol *.",
                                ],
                            },
                            {
                                "role": "model",
                                "parts": [
                                    "course 1 (link)\n course 2 (link)",
                                ],
                            },
                        ]
                    )
                    response = chat_session.send_message(user_input)
                    response_text = response.text

                except Exception as e:
                    error_message = f"An error occurred: {str(e)}"

    except UserProfile.DoesNotExist:
        error_message = "User profile not found. Please complete your profile information."

    return render(request, 'education.html', {'response_text': response_text, 'error_message': error_message})

def donate(request):
    return render(request, 'donate.html')

@login_required
def profile(request):
    user_info = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'user_info': user_info})

def chat(request):
    response_text = None
    user_input = None
    error_message = None

    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        if not user_input:
            error_message = "Please enter a message."
        else:
            try:
                api_key = os.getenv("GOOGLE_API_KEY")
                if not api_key:
                    raise ValueError("API key is missing")

                genai.configure(api_key=api_key)
                generation_config = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 64,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    generation_config=generation_config,
                )
                chat_session = model.start_chat(
                    history=[
                        {
                            "role": "user",
                            "parts": [
                                "You are Sam, a friendly assistant who works for Veteran IT Guide which is a real and registered company",
                            ],
                        },
                        {
                            "role": "model",
                            "parts": [
                                "Hey there! I'm Sam, your friendly assistant at Veteran IT Guide...",
                            ],
                        },
                    ]
                )
                response = chat_session.send_message(user_input)
                response_text = response.text

            except Exception as e:
                error_message = f"An error occurred: {str(e)}"

    return render(request, 'chat.html', {'response_text': response_text, 'user_input': user_input, 'error_message': error_message})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return redirect('/')  # Redirect to home or any other page

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('additional_info')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def additional_info(request):
    if request.method == 'POST':
        form = AdditionalInfoForm(request.POST)
        if form.is_valid():
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.coding_languages = form.cleaned_data['coding_languages']
            user_profile.tech_career_interest = form.cleaned_data['tech_career_interest']
            user_profile.save()
            return redirect('success')
    else:
        form = AdditionalInfoForm()

    return render(request, 'additional_info.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user.userprofile)
    
    return render(request, 'edit-profile.html', {'form': form})

@login_required
def edit_preferences(request):
    return render(request, 'edit_preferences.html')

@login_required
def view_courses(request):
    return render(request, 'courses.html')

def softwareeng(request):
    return render(request, 'lpaths/softwareeng.html')

def cybersec(request):
    return render(request, 'lpaths/cybersecurity.html')

def webdev(request):
    return render(request, 'lpaths/webdev.html')

def networkeng(request):
    return render(request, 'lpaths/neteng.html')

def datasci(request):
    return render(request, 'lpaths/datasci.html')

def dba(request):
    return render(request, 'lpaths/dba.html')

def mobdev(request):
    return render(request, 'lpaths/mobdev.html')

def compprog(request):
    return render(request, 'lpaths/compdev.html')

def netadm(request):
    return render(request, 'lpaths/networkadmin.html')

def cloudcompute(request):
    return render(request, 'lpaths/cloudcompute.html')

def prodmaneg(request):
    return render(request, 'lpaths/producmaneg.html')

def ai(request):
    return render(request, 'lpaths/ai.html')

def ba(request):
    return render(request, 'lpaths/ba.html')

def testing(request):
    return render(request, 'lpaths/testing.html')

def employment(request):
    return render(request, 'employment/employment.html')

def resume(request):
    return render(request, 'employment/resume.html')

def linkedin(request):
    return render(request, 'employment/linkedin.html')

def jobfind(request):
    return render(request, 'employment/jobfind.html')

def contact(request):
    return render(request, 'contact.html')
