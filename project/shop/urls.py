from django.urls import path
from . import views
from project import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('help',views.help,name='help'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]