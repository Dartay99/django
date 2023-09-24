from django.urls import path
from . import views
from project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('help',views.help,name='help'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)