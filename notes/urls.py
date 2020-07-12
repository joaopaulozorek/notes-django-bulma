from django.urls import path
from . import views

urlpatterns = [
	path('', views.notes_list, name='notes_list'),
	path('note/<int:pk>/', views.note_detail, name='note_detail'),
	path('note/new/', views.note_new, name='note_new'),
	path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
]