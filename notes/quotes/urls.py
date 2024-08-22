from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="main"),
    path("add-quote", views.add_quote, name="add-quote"),
]
