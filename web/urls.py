from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("single-event/<int:id>/", views.single_event, name="single_event"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("add-event/", views.add_event, name="add-event"),
    path("form/", views.form, name="form"),
    
    ]