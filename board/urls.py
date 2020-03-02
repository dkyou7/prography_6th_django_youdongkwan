from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('boardList/',BoardList.as_view()),
    path('boardList/<int:pk>/',BoardDetail.as_view()),
]