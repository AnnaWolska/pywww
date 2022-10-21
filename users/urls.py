from django.urls import path
from .views import user_counter, user_detail_view, user_list_view, user_update_view
from django.views.generic import TemplateView
from django.views import defaults as defaults_views


app_name = "users"
urlpatterns = [
    path('~count', view=user_counter, name="counter"),
    path("sometemplate",TemplateView.as_view(template_name="sometemplate.html"),name="sometemplate"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    ]
