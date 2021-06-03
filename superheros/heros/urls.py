from django.urls import path
from . import views




app_name = 'heros'

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_hero'),
    path('<int:hero_id>/delete', views.delete, name='delete'),
    path('<int:hero_id>/edit/', views.edit , name="edit_hero")
]   

