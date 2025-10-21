from django.urls import path
from django.views.generic import TemplateView
from .views import rude_bot_api

urlpatterns = [
    path("", TemplateView.as_view(
        template_name="rudebot/chat.html"), name="chat_page"),
    path("api/chat/", rude_bot_api, name="rude_bot_api"),
]
