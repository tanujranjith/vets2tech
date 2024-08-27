# veteran_it_guide/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guide.urls')),  # Ensure this line is included to link to your app's URLs
        
]
