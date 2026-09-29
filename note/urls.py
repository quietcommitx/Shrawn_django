from django.urls import path, include
from .views import note_list
urlpatterns = [
   path('note/', note_list)
]