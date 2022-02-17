from django.urls import path
from .views import posts_list, first_post, post_details, post_sponsored, add_post, edit_post

app_name = "posts"
urlpatterns = [
    path('',posts_list, name="list"),
    path('<int:post_id>', post_details, name="details"),
    path('add',add_post, name="add_post"),
    path('<int:post_id>/edit', edit_post, name="edit_post")
    ]
