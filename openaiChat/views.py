import openai
from django.shortcuts import render
from django.conf import settings

def chat_view(request):
    response_text = ""
    if request.method == "POST":
        user_message = request.POST.get("message")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            api_key=settings.OPENAI_API_KEY,  # Set your API key in settings
        )
        response_text = response.choices[0].message['content']
    return render(request, "openAIChat/chat.html", {"response": response_text})

