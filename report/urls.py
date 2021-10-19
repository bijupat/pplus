from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('encounter/<int:labkey>/', views.encounter, name='encounter'),
    path('report/<int:repokey>', views.report, name='report'),

]