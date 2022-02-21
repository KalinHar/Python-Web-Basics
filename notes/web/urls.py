from django.urls import path

from notes.web.views import home, add_note, edit_note, delete_note, note_details, profile, add_profile, dell

urlpatterns = (
    path('', home, name='home'),
    path('new/', add_profile, name='add profile'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', note_details, name='note details'),
    path('profile/', profile, name='profile'),
    path('dell/', dell, name='dell'),
)