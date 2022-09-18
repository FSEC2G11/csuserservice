from django.urls import path
from .views import CDAUsersList, CDAUserDetail

urlpatterns = [
    path('users/', CDAUsersList.as_view()),
    path('user/<slug:pk>', CDAUserDetail.as_view()),
]