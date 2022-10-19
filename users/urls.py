from django.urls import path
from .views import user_counter

app_name = "users"
urlpatterns = [
    path('~count', view=user_counter, name="counter"),
    ]
