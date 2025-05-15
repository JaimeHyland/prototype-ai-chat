from django.urls import path
from . import views

app_name = "openAI_chatBot"
urlpatterns = [
    path("", views.chat_view, name="chat"),
]
