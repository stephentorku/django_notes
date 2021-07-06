from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_notes, name='all_notes'),
    path('add', views.add_note, name='add_note'),
    path('view/<str:note_id>', views.view_note, name='view_note'),
    path('delete/<str:note_id>', views.delete_note, name='delete'),
    path('edit/<str:note_id>', views.edit_note, name='edit'),
    path('update/<str:note_id>', views.edit_note, name = 'update')

]
