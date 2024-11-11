from django.urls import path
from pages import views

urlpatterns = [
    path("", views.skill_learning_view, name='home')
]