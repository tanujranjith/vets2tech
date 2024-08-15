import os
import google.generativeai as genai
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from .forms import AdditionalInfoForm, EditProfileForm
from .models import UserProfile

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

import os
import google.generativeai as genai
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AdditionalInfoForm, EditProfileForm
from .models import UserProfile














@login_required
def education(request):
    response_text = None
    error_message = None

    try:
        # Get the user's profile
        user_profile = UserProfile.objects.get(user=request.user)
        coding_interests = user_profile.coding_languages or "Python, JavaScript"  # Default if empty

        if request.method == 'POST':
            user_input = request.POST.get('user_input')

            if not user_input.strip():  # Check if the input is empty or just whitespace
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
                                    f"You are Sam, a friendly assistant who works for Veteran IT Guide. Suggest 10 courses based on the user's coding interests which are: {coding_interests}. The courses should be ordered from beginner to job readiness and include links.",
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













def employment(request):
    return render(request, 'employment.html')

def donate(request):
    return render(request, 'donate.html')

@login_required
def profile(request):
    try:
        user_info = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('additional_info')  # Redirect to a view where users can create their profile

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
                                "You are Sam, a friendly assistant who works for Veteran IT Guide...",
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
            return redirect('additional_info')  # Redirect to additional info form
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
            return redirect('success')  # Redirect to a success page or another view
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
    # Handle the logic for editing preferences
    return render(request, 'edit_preferences.html')

@login_required
def view_courses(request):
    # Logic for the view
    return render(request, 'courses.html')

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def profile_view(request):
    user_info = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'profile.html', {'user_info': user_info})
