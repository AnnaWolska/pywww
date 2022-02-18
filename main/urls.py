from django.urls import path
from main.views import hello_world, my_tests, home_view, contact, user_profile

app_name = "main"
urlpatterns = [
    path('',hello_world, name = "hello"),
    path('tests',my_tests, name = "test"),
    path('home', home_view, name = "home"),
    path('contact', contact, name="contact"),
    path('user/<int:user_id>/profile', user_profile, name="userprofile")
]