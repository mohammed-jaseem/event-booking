from django.urls import path
from manager import views

app_name = "manager"


urlpatterns = [
    path('',views.index, name='index'),
    path('slideries',views.slideries, name='slideries'),
    path('slideries_add',views.slideries_add, name='slideries_add'),
    path('edit_slideries/<int:id>/',views.edit_slideries, name='edit_slideries'),
    path('delete_slideries/<int:id>/',views.delete_slideries, name='delete_slideries'),
    path('events/',views.events, name='events'),
    path('events_add/',views.events_add, name='events_add'),
    path('edit_events/<int:id>/',views.edit_events, name='edit_events'),
    path('delete_events/<int:id>/',views.delete_events, name='delete_events'),
    path('forms/',views.form, name='forms'),
    path('forms_add/',views.forms_add, name='forms_add'),
    path('edit_forms/<int:id>/',views.edit_forms, name='edit_forms'),
    path('delete_forms/<int:id>/',views.delete_forms, name='delete_forms'),
    path('tips/',views.tips, name='tips'),
    path('tips_add/',views.tips_add, name='tips_add'),
    path('edit_tips/<int:id>/',views.edit_tips, name='edit_tips'),
    path('delete_tips/<int:id>/',views.delete_tips, name='delete_tips'),

]