from django.urls import path
from .views import home_view,about_view,action_view,contact_view,doctores_view,news_view

urlpatterns = [
    path('',home_view,name = "home-page"),
    path('about/',about_view,name = "about-page"),
    path('action/',action_view,name = "action-page"),
    path('contact/',contact_view,name = "contact-page"),
    path('doctores/',doctores_view,name = "doctores-page"),
    path('news/',news_view,name = "news-page"),
]
