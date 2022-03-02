from django.urls import path
from .views import galleries_list, gallery_details, add_gallery

app_name = "galleries"
urlpatterns = [
    path('',galleries_list, name="galleries_list"),
    path('<int:gallery_id>', gallery_details, name="gallery_details"),
    path('add', add_gallery, name="add_gallery")
    ]

