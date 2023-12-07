from django.urls import path

from core import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musicos/', views.MusicosView.as_view(), name='musicos'),
    path('musicos/create/', views.MusicosCreateView.as_view(), name='musicos_create'),
    path('musicos/update/<int:pk>/', views.MusicosUpdateView.as_view(), name='musicos_update'),
    path('musicos/delete/<int:pk>/', views.MusicosDeleteView.as_view(), name='musicos_delete'),
]
