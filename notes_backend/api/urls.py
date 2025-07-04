from django.urls import path
from .views import NoteListCreate, NoteDetail, UserCreate, CustomAuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def health(request):
    return Response({"message": "Server is up!"})

urlpatterns = [
    path('health/', health, name='Health'),
    path('register/', UserCreate.as_view(), name='user_create'),
    path('login/', CustomAuthToken.as_view(), name='user_login'),
    path('notes/', NoteListCreate.as_view(), name='note_list_create'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note_detail'),
]
