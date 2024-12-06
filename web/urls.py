from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("booking/", views.booking, name="booking"),
    path("single-event/<int:id>/", views.single_event, name="single_event"),
    ]