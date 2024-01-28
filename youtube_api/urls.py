from django.urls import path
from .views import YouTubeAPI

urlpatterns = [
    path('youtube/', YouTubeAPI.as_view(), name='youtube_api'),
]