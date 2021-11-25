from django.urls import path

from . import views

app_name = 'myweb'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('user_defined', views.user_defined, name = 'user_defined'),
    path('appdev', views.appdev, name = 'appdev'),
    path('intauto', views.intauto, name = 'intauto'),
    path('workimp', views.intauto, name = 'workimp'),
    path('telehealth', views.telehealth, name = 'telehealth'),
    path('website', views.website, name = 'website'),
    path('qa', views.qa, name = 'qa'),
    path('promotor', views.promotor, name = 'promotor'),
    path('coreteam', views.coreteam, name = 'coreteam'),
    path('inquiry', views.inquiry, name = 'inquiry'),
    path('contactus', views.contactus, name = 'contactus'),




   

]