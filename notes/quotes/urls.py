from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="main"),
    path("add-quote", views.add_quote, name="add-quote"),
    path("add-author", views.add_author, name="add-author"),
    path("tag/<str:tag_name>", views.see_tag, name="tag"),
]
