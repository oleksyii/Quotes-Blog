from django.urls import path
from . import views

app_name = "authors"

urlpatterns = [
    path("author/<str:author_id>", views.main, name="author"),
]
