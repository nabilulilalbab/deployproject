from django.urls import path 
from .views import add_feedback, feedback_list
app_name = 'feedback'
urlpatterns = [
        path('', feedback_list, name='list'), 
        path('add/',add_feedback, name='add' )
        ]
