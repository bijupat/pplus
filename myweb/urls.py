from django.urls import path

from . import views

app_name = 'myweb'
urlpatterns = [
    path('', views.index, name = 'index')
]