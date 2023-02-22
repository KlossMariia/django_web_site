from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),#empty space is the main page
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('delete',views.delete, name='delete'),
]
