from django.urls import path

from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musicos/', views.MusicosView.as_view(), name='musicos'),
]
