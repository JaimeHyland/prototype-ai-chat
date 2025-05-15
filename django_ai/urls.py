from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('openAIChat.urls')),  # This includes your app’s URLs[4][7]
]
