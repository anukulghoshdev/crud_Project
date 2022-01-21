from django.contrib import admin
from django.urls import path

from myapp1 import views

app_name = 'my_app1'

urlpatterns = [
    path('',views.home, name='home',),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list' ),
    path('add_musician/', views.musician_form, name='musican_form' ),
    path('add_album_list/', views.album_form, name='album_form'),
    path('edit_artist/<int:artist_id>', views.edit_artist, name="edit_artist"),
    path('edit_album/<int:album_id>', views.edit_album, name="edit_album"),

    path('delete_album/<int:album_id>', views.delete_album, name="delete_album"),
    path('delete_artist/<int:artist_id>', views.delete_artist, name="delete_artist"),

]
