from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_list),
    path('<pk>/', views.song_detail),
]