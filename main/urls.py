from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.s2, name="s2" ),
    path('home/dsa/', views.dsa, name="dsa"),
    path('home/dsa/playlist', views.playlist, name="playlist"),
    path('home/dsa/notes', views.notes, name="notes"),
    path('home/oops', views.oops, name="oops"),
    path('home/dsa/platforms', views.platforms, name="platforms"),
    path('home/dsa/advance_dsa', views.coming, name="advance_dsa"),
    path('home/webdev/', views.webdev, name="webdev"),
    path('home/webdev/frontend_playlists/', views.fplaylist, name='fplaylist'),
    path('home/webdev/backend_playlist/', views.coming, name='coming'),
    path('about/', views.about, name="about"),


]