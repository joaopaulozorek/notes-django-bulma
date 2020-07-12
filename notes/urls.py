from django.urls import path
from . import views

urlpatterns = [
	path('', views.notes_list, name='notes_list'),
	path('note/<int:pk>/', views.note_detail, name='note_detail'),
]