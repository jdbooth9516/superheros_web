from django.urls import path
from . import views




app_name = 'heros'

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_hero'),
    path('delete/<int:hero_id>', views.delete, name='delete'),
    path('edit/<int:hero_id>', views.edit , name="edit_hero")
]   

