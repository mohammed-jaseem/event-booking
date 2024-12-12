from django.urls import path
from manager import views

app_name = "manager"


urlpatterns = [
    path('',views.index, name='index'),
    path('slideries',views.slideries, name='slideries'),
    path('slideries_add',views.slideries_add, name='slideries_add'),
    path('edit_slideries/<int:id>/',views.edit_slideries, name='edit_slideries'),
    path('delete_slideries/<int:id>/',views.delete_slideries, name='delete_slideries'),
]