from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pejuma_app-home'),
    path('about/', views.about, name='pejuma_app-about'),
    path('contact/', views.contact, name='pejuma_app-contact'),
    path('terms/', views.terms, name='pejuma_app-terms'),
    path('categories/', views.categories, name='pejuma_app-categories'),
]